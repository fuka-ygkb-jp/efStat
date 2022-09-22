#!/usr/bin/perl
require 5.004;	# 本プログラムは(少なくとも)perl 5.004以上を必要とします。
$ver = '2.2.4';	# 本プログラムのバージョン。変更しないで下さい。
;#+------------------------------------------------------------------------
;#|efStat[ログ表示部]
;#|(C)1998-2016 不可思議絵の具(https://ygkb.jp/)
;#+------------------------------------------------------------------------
;#|インターフェース部(操作画面)
;#+------------------------------------------------------------------------
;# ●●●●●●●●●●●● ユーザ側設定(ここから) ●●●●●●●●●●●●
;#+------------------------------------------------------------------------
;# [重要な設定] (この設定は絶対に必要です!!)
;#+------------------------------------------------------------------------
;# [ログファイルを格納したディレクトリの名前]
;# ログ用ディレクトリは fstat/ 以下に作って下さい。
$Dir_Log = 'log';


;# [あなたのサイトのURL]
;# 「サイト内移動分析」の起点となります。　入力は正確に。
;# index.htmlなどは不要です(…というか、あると不都合)。
;# また、この項目を空にすると正常に動作しません。
@MySite = (
	'http://ygkb.jp/',
	'https://ygkb.jp/',
	'http://yugen.pya.jp/',
	'http://yugenk.seesaa.net/',
	'http://xxx.yourdomain.com/~username/',
);


# [パスワードで閲覧制限するか]
# この値を 1 にすると、閲覧の際には必ずパスワード入力が必要になります。
$DoPass = 0;

# [その場合のパスワード]
$Pass = 'abc';


# [まとめたいURL]
@Complete_URL = (
	[ 'fstat.cgi', 'efStatコピーライトから' ],
	[ 'listgen_c.cgi', 'Listgenコピーライトから' ],
	[ 't.co', 'Twitter' ],
);


;#+------------------------------------------------------------------------
;# [表示オプション] (この指定はログ指定モードで有効です)
;#+------------------------------------------------------------------------
;# [参照元へのリンクを有効にするか・しないか]
;# 1 で有効。　0 だと無効(ただのテキストになる)。
$DoLink = 1;

;# [表示をテイストレスにするか・しないか]
;# 表に色が付かなくなります。　代わりに、表示が速くなります。
;# 1 で有効。　0 だと表に色が付きます。
$DoTasteless = 0;

;# [グラフを表示させるか・させないか]
;# 1 で表示。　0 だとグラフが表示されなくなります。
$DoPutGraph = 1;


;#+------------------------------------------------------------------------
;# [表の足切り設定(表示リミッタ)] (この指定はログ指定モードで有効です)
;#+------------------------------------------------------------------------
;# [生ログ表示]
;# 最新の ｎ 件まで表示するようになります。 0以上。
;# efCountで設定した「最大ログ保存数」以上にならないようにして下さい。
$Limit_Log  = 50;

;# 解析表の中で、この数以下は表示されません。
;# 省略しない場合は 0 を指定して下さい。
$Limit_Ref    = 0;	# [参照元解析]
$Limit_Search = 0;	# [サーチエンジンのキーワード]

$Limit_Host   = 10;	# [ホスト名解析]
$Limit_Domain = 0;	# [国籍分析]

$Limit_Agent  = 0;	# [ブラウザ解析]


;#+------------------------------------------------------------------------
;# [ページ表示指定]
;#+------------------------------------------------------------------------
;# [表示色]
$html_body  = '<BODY background="./lib/w.jpg" text=#7e2828 link=#7726c8 alink=#5c4fff vlink=#ff5959>';

$tbc[0] = 'bgcolor=#fcfcfc';	# [テーブル背景色 (見出し)]    #灰
$tbc[1] = 'bgcolor=#ff9090';	# [テーブル背景色 (項目1列目)] #赤
$tbc[2] = 'bgcolor=#ffd092';	# [テーブル背景色 (項目2列目)] #橙
$tbc[3] = 'bgcolor=#acffb6';	# [テーブル背景色 (項目4列目)] #緑
$tbc[4] = 'bgcolor=#c6c6ff';	# [テーブル背景色 (項目3列目)] #紫
$tbc[5] = 'bgcolor=#ffbfbf';	# [テーブル背景色 (内容1列目)] #赤
$tbc[6] = 'bgcolor=#ffdfbf';	# [テーブル背景色 (内容2列目)] #橙
$tbc[7] = 'bgcolor=#d5ffd5';	# [テーブル背景色 (内容3列目)] #緑
$tbc[8] = 'bgcolor=#dfdfff';	# [テーブル背景色 (内容4列目)] #紫
$tbc[9] = 'bgcolor=#bfdfdf';	# [テーブル背景色 (内容5列目)] #深緑?

;# [ワンポイントアドバイス]
;# 必ずしも 'bgcolor=' で始める必要はありません。
;# 'background=画像ファイル' と指定するとテーブル背景に画像が使えます。


;# おまけ / 1にすると計算に掛かった時間を表示します。
;# 何やら機種依存の強そうな関数を使っていますので、動かなかったら諦めて下さい。
$DoPutBenchmark =  1;

;#+------------------------------------------------------------------------
;#|●●●●●●●●●●●● ユーザ側設定(ここまで) ●●●●●●●●●●●●
;#+------------------------------------------------------------------------
require "./lib/start.pl";
