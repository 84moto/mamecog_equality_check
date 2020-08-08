# mamecog_equality_check

まめコグ（[https://github.com/84moto/mamecog](https://github.com/84moto/mamecog)）とKerasの出力が同等であることを確認するためのツール

## 使用方法

この例では、[https://github.com/84moto/mamecog](https://github.com/84moto/mamecog)にあるmamecog（まめコグ）のSample.csの出力をKerasの出力と比較します。

[https://github.com/84moto/mamecog](https://github.com/84moto/mamecog)の例と同様に、KerasでCNNの学習済みモデルをmy_model.h5として保存し、dump_pool_output.pyを実行すると、下記のように２つめのプーリング層の出力が表示されます。

```
Plane 0
0.0378 0.1151 0.0000 0.0000 0.0000
0.0000 0.0000 0.0000 0.0000 0.0000
0.0000 0.0000 0.0000 0.0000 0.0000
0.0000 0.0000 0.0000 0.0000 0.0000
0.0000 0.0000 0.0000 0.0000 0.0000
Plane 1
0.1318 0.0000 0.0000 0.1170 0.0000
0.0000 0.0000 0.0000 0.0000 0.0000
0.0000 0.0000 0.0000 0.4471 0.0000
0.0000 0.0000 0.1142 0.3167 0.0000
0.0000 0.0912 0.7771 0.0000 0.0000
Plane 2
0.9758 0.0000 0.0000 0.0000 0.0000
0.4625 0.0000 0.0000 0.0000 0.0000
0.0000 0.0000 0.6534 0.8755 0.1980
0.0000 0.1900 1.4270 0.0000 0.4992
0.0000 1.4729 1.5649 0.3348 0.4539
 ・
 ・
 ・
```

まめコグ（[https://github.com/84moto/mamecog](https://github.com/84moto/mamecog)）の
Sample.csのMain関数の末尾に下記のコードを追加すると、
上記のdump_pool_output.pyの場合と同様にプーリング層の値が表示されるので、
Diffツール等を用いて両者を比較します。

```
pool2output.PrintCellValues();
```

## ライセンス

mamecog_equality_checkは、MITライセンスで公開します。
"as is"（現状のまま）の提供です。一切の保証はありません。
ご使用は自己責任でお願いします。

## 開発者

mamecog_equality_checkの開発者は、Hideki Hashimoto（84moto）です。
ご連絡は[https://twitter.com/hashimov](https://twitter.com/hashimov)にお願いします。

