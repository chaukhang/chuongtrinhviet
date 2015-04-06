#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib , urllib2 , re , zlib , os , uuid , json
from xbmcswift2 import Plugin , xbmc , xbmcgui , xbmcaddon
oo000 = Plugin ( )
ii = "plugin://plugin.video.phim60s.info"
oOOo = 10
if 59 - 59: Oo0Ooo . OO0OO0O0O0 * iiiIIii1IIi . iII111iiiii11 % I1IiiI
@ oo000 . route ( '/' )
def IIi1IiiiI1Ii ( ) :
 I11i11Ii ( "None" , "None" )
 oO00oOo = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 if 6 - 6: i1 * ii1IiI1i % OOooOOo / I11i / o0O / IiiIII111iI
 IiII = [
 { 'label' : 'Phim mới' , 'path' : '%s/latest/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/film-new.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Phim hot' , 'path' : '%s/hottest/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/film-hot.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Phim lẻ' , 'path' : '%s/movies/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/film-le.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Phim bộ' , 'path' : '%s/series/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/film-bo.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Theo thể loại' , 'path' : '%s/genres' % ii } ,
 { 'label' : 'Theo Quốc gia' , 'path' : '%s/nations' % ii } ,
 { 'label' : 'Tìm kiếm' , 'path' : '%s/search' % ii }
 ]
 return oo000 . finish ( IiII )
 if 28 - 28: Ii11111i * iiI1i1
@ oo000 . route ( '/latest/<murl>/<page>' )
def i1I1ii1II1iII ( murl , page ) :
 I11i11Ii ( "Browse" , '/latest/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'latest' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 53 - 53: o0oo0o / Oo + OOo00O0Oo0oO / iIi * ooO00oOoo - O0OOo
@ oo000 . route ( '/hottest/<murl>/<page>' )
def II1Iiii1111i ( murl , page ) :
 I11i11Ii ( "Browse" , '/hottest/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'hottest' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 25 - 25: OOo000
@ oo000 . route ( '/movies/<murl>/<page>' )
def O0 ( murl , page ) :
 I11i11Ii ( "Browse" , '/movies/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'movies' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 34 - 34: ooO00oOoo % i1 % iiiIIii1IIi % ooO00oOoo * iIi / o0O
@ oo000 . route ( '/series/<murl>/<page>' )
def Iiii ( murl , page ) :
 I11i11Ii ( "Browse" , '/series/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'series' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 87 - 87: iiI1i1 / OOo000 + O0OOo - OOo000 . OOo000 / i1
@ oo000 . route ( '/genres' )
def iiIIIIi1i1 ( ) :
 I11i11Ii ( "Browse" , '/genres' )
 IiII = [
 { 'label' : 'Hành Động' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/hanh-dong-1.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Võ Thuật' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/vo-thuat-2.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Chiến Tranh' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/chien-tranh-3.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Hình Sự' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/hinh-su-4.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Hoạt Hình' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/hoat-hinh-5.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Kinh Dị & Ma' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/kinh-di-ma-6.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Hài Hước' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/hai-huoc-7.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Viễn Tưởng' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/vien-tuong-8.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Phiêu Lưu' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/phieu-luu-9.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Thần Thoại' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/than-thoai-10.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Truyền Hình' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/truyen-hinh-11.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Cổ Trang' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/co-trang-12.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Tâm Lý' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/tam-ly-16.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Gia Đình' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/gia-dinh-15.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Tình Cảm' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/tinh-cam-17.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Thể Thao' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/the-thao-18.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Âm Nhạc' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/am-nhac-19.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Tài Liệu' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/tai-lieu-20.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Tiểu Sử' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/tieu-su-29.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Bí Ẩn' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/bi-an-23.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Giật Gân' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/giat-gan-24.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Lịch Sử' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/lich-su-25.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Viễn Tây' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/vien-tay-30.html?p=%s' ) , 1 ) }
 ]
 return oo000 . finish ( IiII )
 if 54 - 54: o0oo0o % OO0OO0O0O0 + ii1IiI1i - iIi / Oo
@ oo000 . route ( '/genres/<murl>/<page>' )
def iIiiI1 ( murl , page = 1 ) :
 I11i11Ii ( "Browse" , '/genres/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'genres' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 68 - 68: ii1IiI1i - Oo0Ooo - I11i / o0oo0o - I11i + I1IiiI
@ oo000 . route ( '/nations' )
def IiiIII111ii ( ) :
 I11i11Ii ( "Browse" , '/nations' )
 IiII = [
 { 'label' : 'Việt Nam' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/country/viet-nam-1.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Hàn Quốc' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/country/han-quoc-2.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Nhật Bản' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/country/nhat-ban-3.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Trung Quốc' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/country/trung-quoc-4.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Mỹ - Châu Âu' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/country/my-chau-au-5.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Hồng Kong' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/country/hong-kong-6.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Đài Loan' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/country/dai-loan-7.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Châu Á' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/country/chau-a-8.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Ấn Độ' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/country/an-do-10.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Thái Lan' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/country/thai-lan-11.html?p=%s' ) , 1 ) }
 ]
 return oo000 . finish ( IiII )
 if 3 - 3: iIi + OO0OO0O0O0
@ oo000 . route ( '/nations/<murl>/<page>' )
def I1Ii ( murl , page ) :
 I11i11Ii ( "Browse" , '/nations/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'nations' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 66 - 66: OOo00O0Oo0oO
@ oo000 . route ( '/search/' )
def oo0Ooo0 ( ) :
 I11i11Ii ( "Browse" , '/search' )
 I1I11I1I1I = oo000 . keyboard ( heading = 'Tìm kiếm' )
 if I1I11I1I1I :
  OooO0OO = "http://m.phim60s.info/tim-kiem.html?keyword=&p=%s" . replace ( "keyword=" , "keyword=" + I1I11I1I1I . replace ( " " , "+" ) )
  iiiIi = '%s/search/%s/%s' % ( ii , urllib . quote_plus ( OooO0OO ) , 1 )
  oo000 . redirect ( iiiIi )
  if 24 - 24: OO0OO0O0O0 % IiiIII111iI + I1IiiI + O0OOo + Ii11111i
@ oo000 . route ( '/search/<murl>/<page>' )
def OOoO000O0OO ( murl , page ) :
 I11i11Ii ( "Browse" , '/search/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'search' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 23 - 23: Oo0Ooo + ii1IiI1i
@ oo000 . route ( '/mirrors/<murl>' )
def oOo ( murl ) :
 I11i11Ii ( "Browse" , '/mirrors/%s' % ( murl ) )
 IiII = [ ]
 for oOoOoO in ii1I ( murl ) :
  if "Zing" not in oOoOoO [ "name" ] and "ClipVN" not in oOoOoO [ "name" ] :
   OooO0 = { }
   OooO0 [ "label" ] = oOoOoO [ "name" ] . strip ( )
   II11iiii1Ii = str ( uuid . uuid1 ( ) )
   OO0o = oo000 . get_storage ( II11iiii1Ii )
   OO0o [ "list" ] = oOoOoO [ "eps" ]
   OooO0 [ "path" ] = '%s/eps/%s' % ( ii , urllib . quote_plus ( II11iiii1Ii ) )
   IiII . append ( OooO0 )
 return oo000 . finish ( IiII )
 if 82 - 82: Oo0Ooo . o0oo0o / OOooOOo * OO0OO0O0O0 % iiI1i1 % iiiIIii1IIi
@ oo000 . route ( '/eps/<eps_list>' )
def Oo00OOOOO ( eps_list ) :
 I11i11Ii ( "Browse" , '/eps' )
 IiII = [ ]
 for O0O in oo000 . get_storage ( eps_list ) [ "list" ] :
  OooO0 = { }
  OooO0 [ "label" ] = O0O [ "name" ] . strip ( )
  OooO0 [ "is_playable" ] = True
  OooO0 [ "path" ] = '%s/play/%s' % ( ii , urllib . quote_plus ( O0O [ "url" ] ) )
  IiII . append ( OooO0 )
 return oo000 . finish ( IiII )
 if 83 - 83: Oo + i1 * IiiIII111iI % I11i + Oo
@ oo000 . route ( '/play/<url>' )
def Ii1iIIIi1ii ( url ) :
 I11i11Ii ( "Play" , '/play/%s' % ( url ) )
 o0oo0o0O00OO = xbmcgui . DialogProgress ( )
 o0oo0o0O00OO . create ( 'phim60s.info' , 'Loading video. Please wait...' )
 oo000 . set_resolved_url ( o0oO ( url ) )
 o0oo0o0O00OO . close ( )
 del o0oo0o0O00OO
 if 48 - 48: Oo + Oo / i1 / iiiIIii1IIi
def o0oO ( url ) :
 i1iiI11I = iiii ( url )
 oO0o0O0OOOoo0 = re . compile ( 'source src="(http://m.phim60s.info/.+?.mp4)"' ) . findall ( i1iiI11I ) [ 0 ]
 if "youtube" in i1iiI11I :
  IiIiiI = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( i1iiI11I )
  I1I = IiIiiI [ 0 ] [ len ( IiIiiI [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  return 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % I1I
 if "picasa" in i1iiI11I :
  oOO00oOO = re . compile ( 'src="(http://m.phim60s.info/picasa-sd/.+?.mp4)"' ) . findall ( i1iiI11I ) [ 0 ]
  if oo000 . get_setting ( 'HQ' , bool ) :
   if "lh/photo" not in i1iiI11I :
    OoOo = ""
    if "authkeyenterplus" in oOO00oOO :
     iI , o00O , OOO0OOO00oo = re . compile ( 'http://m.phim60s.info/picasa-sd/(\d+)/\w+authkeyenterplus(.+?)/daukhac/(\d+).mp4' ) . findall ( oOO00oOO ) [ 0 ]
     OoOo = "https://picasaweb.google.com/data/feed/api/user/%s/photoid/%s?authkey=%s&alt=json" % ( iI , OOO0OOO00oo , o00O )
    else :
     iI , OOO0OOO00oo = re . compile ( 'http://m.phim60s.info/picasa-sd/(\d+)/\w+/daukhac/(\d+).mp4' ) . findall ( oOO00oOO ) [ 0 ]
     OoOo = "https://picasaweb.google.com/data/feed/api/user/%s/photoid/%s?alt=json" % ( iI , OOO0OOO00oo )
    i1iiI11I = urllib2 . urlopen ( OoOo ) . read ( )
    Iii111II = json . loads ( i1iiI11I ) [ "feed" ] [ "media$group" ] [ "media$content" ]
    for iiii11I in Iii111II :
     if ( iiii11I [ "type" ] == "video/mpeg4" ) and ( int ( iiii11I [ "height" ] ) <= 720 ) :
      oO0o0O0OOOoo0 = iiii11I [ "url" ]
   else :
    oOO00oOO = oOO00oOO . replace ( "http://m.phim60s.info/picasa-sd/" , "https://picasaweb.google.com/" ) . strip ( ".mp4" )
    i1iiI11I = urllib2 . urlopen ( oOO00oOO ) . read ( )
    OoOo = re . compile ( '(https://picasaweb.google.com/data/feed/tiny/user/\d+/photoid/\d+\?alt=jsonm&gupi=.+?)"' ) . findall ( i1iiI11I ) [ 0 ]
    i1iiI11I = urllib2 . urlopen ( OoOo ) . read ( )
    Iii111II = json . loads ( i1iiI11I ) [ "feed" ] [ "media" ] [ "content" ]
    for iiii11I in Iii111II :
     if ( iiii11I [ "type" ] == "video/mpeg4" ) and ( int ( iiii11I [ "height" ] ) <= 720 ) :
      oO0o0O0OOOoo0 = iiii11I [ "url" ]
 return oO0o0O0OOOoo0
 if 96 - 96: i1 % OOo00O0Oo0oO . o0oo0o + iII111iiiii11 * iiI1i1 - o0O
def oooO0oo0oOOOO ( url , page , route_name ) :
 i11i1 = int ( page ) + 1
 i1iiI11I = iiii ( url % page )
 IiIiiI = re . compile ( '<a href="(http://m.phim60s.info/watch/.+?)"><img[^>]*src="(.+?)"><h2>(.+?)</h2><p>(.+?)</p>' ) . findall ( i1iiI11I )
 IiII = [ ]
 for IIIii1II1II , i1I1iI , oo0OooOOo0 , o0OO00oO in IiIiiI :
  OooO0 = { }
  OooO0 [ "label" ] = "%s - %s" % ( oo0OooOOo0 , o0OO00oO )
  OooO0 [ "thumbnail" ] = i1I1iI
  OooO0 [ "path" ] = '%s/%s/%s' % ( ii , "mirrors" , urllib . quote_plus ( IIIii1II1II ) )
  IiII . append ( OooO0 )
 if len ( IiII ) == oOOo :
  IiII . append ( { 'label' : 'Next >>' , 'path' : '%s/%s/%s/%s' % ( ii , route_name , urllib . quote_plus ( url ) , i11i1 ) , 'thumbnail' : 'http://icons.iconarchive.com/icons/rafiqul-hassan/blogger/128/Arrow-Next-icon.png' } )
 return IiII
 if 39 - 39: ooO00oOoo - i1 * I11i % IiiIII111iI * i1 % i1
def ii1I ( murl ) :
 i1iiI11I = iiii ( murl )
 IiIiiI = re . compile ( '</script><br/>(.+?)<br/></div>' ) . findall ( i1iiI11I )
 OoOOOOO = IiIiiI [ 0 ] . split ( "<br/>" )
 iIi1i111II = re . compile ( '<title>(.+?)</title>' ) . findall ( i1iiI11I ) [ 0 ]
 OoOO00O = [ ]
 for oOoOoO in OoOOOOO :
  oOOoO0O0O0 = re . compile ( '(.+?):<' ) . findall ( oOoOoO ) [ 0 ] . strip ( )
  Oo000o = [ ]
  for I11IiI1I11i1i , iI1ii1Ii in re . compile ( '<a href="(.+?)"[^>]*>(.+?)</a>' ) . findall ( oOoOoO ) :
   O0O = { }
   O0O [ "url" ] = I11IiI1I11i1i
   O0O [ "name" ] = "Part %s - %s" % ( iI1ii1Ii , iIi1i111II )
   Oo000o . append ( O0O )
  oOoOoO = { }
  oOoOoO [ "name" ] = oOOoO0O0O0
  oOoOoO [ "eps" ] = Oo000o
  OoOO00O . append ( oOoOoO )
 return OoOO00O
 if 92 - 92: o0O
@ oo000 . cached ( TTL = 60 )
def iiii ( url ) :
 i1OOO = urllib2 . Request ( url )
 i1OOO . add_header ( 'User-Agent' , 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3' )
 i1OOO . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' )
 i1OOO . add_header ( 'Accept-Encoding' , 'gzip, deflate, sdch' )
 Oo0oOOo = urllib2 . urlopen ( i1OOO )
 Oo0OoO00oOO0o = Oo0oOOo . read ( )
 Oo0oOOo . close ( )
 if "gzip" in Oo0oOOo . info ( ) . getheader ( 'Content-Encoding' ) :
  Oo0OoO00oOO0o = zlib . decompress ( Oo0OoO00oOO0o , 16 + zlib . MAX_WBITS )
 Oo0OoO00oOO0o = '' . join ( Oo0OoO00oOO0o . splitlines ( ) ) . replace ( '\'' , '"' )
 Oo0OoO00oOO0o = Oo0OoO00oOO0o . replace ( '\n' , '' )
 Oo0OoO00oOO0o = Oo0OoO00oOO0o . replace ( '\t' , '' )
 Oo0OoO00oOO0o = re . sub ( '  +' , ' ' , Oo0OoO00oOO0o )
 Oo0OoO00oOO0o = Oo0OoO00oOO0o . replace ( '> <' , '><' )
 return Oo0OoO00oOO0o
 if 80 - 80: iiI1i1 + o0oo0o - o0oo0o % iIi
OoOO0oo0o = xbmc . translatePath ( xbmcaddon . Addon ( 'plugin.video.phim60s.info' ) . getAddonInfo ( 'profile' ) )
if 14 - 14: IiiIII111iI * iIi * iIi / o0O
if os . path . exists ( OoOO0oo0o ) == False :
 os . mkdir ( OoOO0oo0o )
Oo0o00 = os . path . join ( OoOO0oo0o , 'visitor' )
if 73 - 73: iIi * OOo00O0Oo0oO + IiiIII111iI . o0oo0o + Ii11111i % iIi
if os . path . exists ( Oo0o00 ) == False :
 from random import randint
 oo0O = open ( Oo0o00 , "w" )
 oo0O . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 oo0O . close ( )
 if 92 - 92: iIi . O0OOo
def i1i ( utm_url ) :
 iiI111I1iIiI = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  i1OOO = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : iiI111I1iIiI }
 )
  Oo0oOOo = urllib2 . urlopen ( i1OOO ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return Oo0oOOo
 if 41 - 41: OOooOOo . OOo000 + OO0OO0O0O0 * IiiIII111iI % OOooOOo * OOooOOo
def I11i11Ii ( group , name ) :
 try :
  try :
   from hashlib import md5
  except :
   from md5 import md5
  from random import randint
  import time
  from urllib import unquote , quote
  from os import environ
  from hashlib import sha1
  iIIIIi1iiIi1 = "1.0"
  iii1i1iiiiIi = open ( Oo0o00 ) . read ( )
  IiiiOO0OoO0o00 = "Phim60s"
  ooOO0O0ooOooO = "UA-52209804-2"
  oOOOo00O00oOo = "www.viettv24.com"
  iiIIIi = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   ooo00OOOooO = iiIIIi + "?" + "utmwv=" + iIIIIi1iiIi1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( IiiiOO0OoO0o00 ) + "&utmac=" + ooOO0O0ooOooO + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , iii1i1iiiiIi , "1" , "1" , "2" ] )
   if 67 - 67: Oo * iiI1i1 * Ii11111i + o0oo0o / I1IiiI
   if 11 - 11: OOo00O0Oo0oO + iIi - OOo000 * iiI1i1 % Oo0Ooo - O0OOo
   if 83 - 83: Oo / ii1IiI1i
   if 34 - 34: ooO00oOoo
   if 57 - 57: iiI1i1 . Oo . I1IiiI
  else :
   if group == "None" :
    ooo00OOOooO = iiIIIi + "?" + "utmwv=" + iIIIIi1iiIi1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( IiiiOO0OoO0o00 + "/" + name ) + "&utmac=" + ooOO0O0ooOooO + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , iii1i1iiiiIi , "1" , "1" , "2" ] )
    if 42 - 42: Oo + Ii11111i % OO0OO0O0O0
    if 6 - 6: iiI1i1
    if 68 - 68: o0O - I11i
    if 28 - 28: I11i . o0oo0o / o0oo0o + OOooOOo . Ii11111i
    if 1 - 1: iiiIIii1IIi / i1
   else :
    ooo00OOOooO = iiIIIi + "?" + "utmwv=" + iIIIIi1iiIi1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( IiiiOO0OoO0o00 + "/" + group + "/" + name ) + "&utmac=" + ooOO0O0ooOooO + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , iii1i1iiiiIi , "1" , "1" , "2" ] )
    if 33 - 33: Oo
    if 18 - 18: IiiIII111iI % iIi * OO0OO0O0O0
    if 87 - 87: Oo0Ooo
    if 93 - 93: Ii11111i - I11i % Oo0Ooo . iIi / iIi - O0OOo
    if 9 - 9: Ii11111i / OOooOOo - ii1IiI1i / iII111iiiii11 / iiiIIii1IIi - IiiIII111iI
    if 91 - 91: iIi % I1IiiI % iiiIIii1IIi
  print "============================ POSTING ANALYTICS ============================"
  i1i ( ooo00OOOooO )
  if 20 - 20: o0oo0o % OOo00O0Oo0oO / OOo00O0Oo0oO + OOo00O0Oo0oO
  if not group == "None" :
   III1IiiI = iiIIIi + "?" + "utmwv=" + iIIIIi1iiIi1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( oOOOo00O00oOo ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + IiiiOO0OoO0o00 + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( IiiiOO0OoO0o00 ) + "&utmac=" + ooOO0O0ooOooO + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , iii1i1iiiiIi , "1" , "2" ] )
   if 31 - 31: IiiIII111iI . ii1IiI1i
   if 46 - 46: iIi
   if 8 - 8: iiI1i1 * o0O - OOo00O0Oo0oO - I11i * o0oo0o % ii1IiI1i
   if 48 - 48: OO0OO0O0O0
   if 11 - 11: Oo + iII111iiiii11 - I11i / IiiIII111iI + OOooOOo . i1
   if 41 - 41: OOo00O0Oo0oO - OO0OO0O0O0 - OO0OO0O0O0
   if 68 - 68: o0oo0o % O0OOo
   if 88 - 88: iiiIIii1IIi - OOo000 + o0oo0o
   try :
    print "============================ POSTING TRACK EVENT ============================"
    i1i ( III1IiiI )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 40 - 40: ii1IiI1i * OOo00O0Oo0oO + o0oo0o % iIi
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 74 - 74: iiI1i1 - OOooOOo + iII111iiiii11 + O0OOo / o0O
if __name__ == '__main__' :
 oo000 . run ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
