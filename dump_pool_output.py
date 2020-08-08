#
# dump_pool_output.py
# Copyright © 2020 Hideki Hashimoto
#
# https://github.com/84moto/mamecog_equality_check
#
# This software is released under the MIT License.
#

# mamecog（まめコグ）とKerasの出力の同等性の確認のため
# テスト入力に対するプーリング層の出力を表示する

import numpy as np
import tensorflow as tf
from tensorflow import keras

# 学習済みの.h5ファイルを読み込む
model = keras.models.load_model("my_model.h5")
model.summary()

# 公開されているMNISTの画像データを読み込む
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# 入力データを整形する
x_test = x_test.astype("float32") / 255
x_test = np.expand_dims(x_test, -1)

# 中間層まで計算するmodelを作成する
intermediate_layer_model = keras.models.Model(inputs=model.input, outputs=model.get_layer("max_pooling2d_1").output)
intermediate_layer_model.summary()

# 中間層出力をmodel.predictで得る
intermediate_outputs = intermediate_layer_model.predict(x_test)
print(intermediate_outputs.shape)

# 今回はmamecogとの比較サンプルとしてx_testの1万個の画像データのうち
# 0番目を入力したときの出力を表示することとする
x1_output = intermediate_outputs[0]

# まめコグのMaxPool2DクラスのPrintCellValues()メソッドと
# 同じ形式でレイヤーの出力値を表示する
plane_num = x1_output.shape[2]
for plane_idx in range(plane_num):
    print("Plane", plane_idx)
    #print(x1_output[:, :, plane_idx])
    for row in range(x1_output.shape[1]):
        for col in range(x1_output.shape[0]):
            v = x1_output[row, col, plane_idx]
            print('{:.4f} '.format(v), end="")
        print('')

#end
