# ansible-role-apache2 [![Build Status](https://travis-ci.org/izumimatsuo/ansible-role-apache2.svg?branch=master)](https://travis-ci.org/izumimatsuo/ansible-role-apache2)

CentOS 7 に Apache Web サーバを構築する ansible role です。

以下のセキュリティ設定を反映済み。

* サーバ情報の隠蔽
* ディレクトリリスティングの無効化
* クリックジャッキング対策
* クロスサイトスクリプティング対策

## 設定項目

以下の設定項目は上書き可能。

項目名             |デフォルト値|説明
-------------------|------------|----------
apache2_listen_port|80          |ポート番号
apache2_server_name|localhost   |サーバ名

## ログフォーマット

以下の内容を出力。

項目名        |説明
--------------|------------------------------
%h            |リモートホスト名
%l            |リモートログ名 "-" 表示
%u            |リモートユーザ
%t            |リクエストを受け付けた日時
%r            |リクエストの最初の行
%>s           |ステータスコード
%b            |レスポンスのバイト数
%{Referer}i   |リファラー
%{User-Agent}i|エージェント
%D            |レスポンス時間、マイクロ秒単位
