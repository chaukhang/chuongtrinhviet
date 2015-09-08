import CommonFunctions as common
import urllib
import urllib2
import os
import xbmcplugin
import xbmcgui
import xbmcaddon
import urlfetch
import re
import json
from BeautifulSoup import BeautifulSoup

__settings__ = xbmcaddon.Addon(id='plugin.video.hdplay')
__language__ = __settings__.getLocalizedString
home = __settings__.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
thumbnails = xbmc.translatePath( os.path.join( home, 'thumbnails\\' ) )

def _makeCookieHeader(cookie):
	cookieHeader = ""
	for value in cookie.values():
			cookieHeader += "%s=%s; " % (value.key, value.value)
	return cookieHeader

def make_request(url, headers=None):
	if headers is None:
			headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
								 'Referer' : 'http://www.google.com'}
	try:
			req = urllib2.Request(url,headers=headers)
			f = urllib2.urlopen(req)
			body=f.read()
			return body
	except urllib2.URLError, e:
			print 'We failed to open "%s".' % url
			if hasattr(e, 'reason'):
					print 'We failed to reach a server.'
					print 'Reason: ', e.reason
			if hasattr(e, 'code'):
					print 'We failed with error code - %s.' % e.code
#def get_fpt():
	add_link('', 'Fashion TV', 0, 'http://hlscache.fptplay.net.vn/sopchannel/fashiontv.stream/playlist.m3u8', '', '')
	add_link('', 'MTV', 0, 'http://hlscache.fptplay.net.vn/sopchannel/mtvviet.stream/playlist.m3u8', '', '')
	add_link('', 'Star World', 0, 'http://hlscache.fptplay.net.vn/sopchannel/starworld.stream/playlist.m3u8', '', '')
	add_link('', 'Cinemax', 0, 'http://hlscache.fptplay.net.vn/sopchannel/cinemax.stream/playlist.m3u8', '', '')
	add_link('', 'Discovery Channel', 0, 'http://hlscache.fptplay.net.vn/sopchannel/discoverychannel.stream/playlist.m3u8', '', '')
	add_link('', 'Channel V', 0, 'http://hlscache.fptplay.net.vn/sopchannel/channelv.stream/playlist.m3u8', '', '')
	add_link('', 'Cartoon Network', 0, 'http://hlscache.fptplay.net.vn/sopchannel/cartoonnetwork.stream/playlist.m3u8', '', '')
	add_link('', 'Animal Planet', 0, 'http://hlscache.fptplay.net.vn/sopchannel/animalplanet.stream/playlist.m3u8', '', '')
	add_link('', 'National Geographic', 0, 'http://hlscache.fptplay.net.vn/sopchannel/nationalgeographic.stream/playlist.m3u8', '', '')
	add_link('', 'National Geographic Adventure', 0, 'http://hlscache.fptplay.net.vn/sopchannel/nationalgeographicadventure.stream/playlist.m3u8', '', '')
	add_link('', 'Nation Geographic Wild', 0, 'http://hlscache.fptplay.net.vn/sopchannel/nationalgeographicwild.stream/playlist.m3u8', '', '')
	add_link('', 'True Visions', 0, 'http://hlscache.fptplay.net.vn/sopchannel/truevisions.stream/playlist.m3u8', '', '')
	add_link('', 'Net TV Sport 1', 0, 'http://hlscache.fptplay.net.vn/event/sport1/playlist.m3u8', '', '')
	add_link('', 'Net TV Sport 2', 0, 'http://hlscache.fptplay.net.vn/event/sport2/playlist.m3u8', '', '')
	add_link('', 'Net TV Sport 3', 0, 'http://hlscache.fptplay.net.vn/event/sport3/playlist.m3u8', '', '')
	add_link('', 'Net TV Sport 4', 0, 'http://hlscache.fptplay.net.vn/event/sport4/playlist.m3u8', '', '')
	add_link('', 'Star Sport', 0, 'http://hlscache.fptplay.net.vn/sopchannel/starsports.stream/playlist.m3u8', '', '')
	add_link('', 'FOX Sport', 0, 'http://hlscache.fptplay.net.vn/sopchannel/foxsports.stream/playlist.m3u8', '', '')

	content = make_request('http://play.fpt.vn/livetv/')
	soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
	items = soup.findAll('a', {'class' : 'channel_link'})
	for item in items:
		img = item.find('img')
		if img is not None:
			try:
				add_link('', item['channel'], 0, 'http://play.fpt.vn' + item['href'], img['src'], '')
			except:
				pass
#add_dir(name,url,mode,iconimage,query='',type='f',page=0):
def get_vtc_movies(url, query='25', type='', page=0):
	if url == '':
		content = make_request('http://117.103.206.21:88/Movie/GetMovieGenres?device=4')
		result = json.loads(content)
		for item in result:
			add_dir(item["Name"], 'http://117.103.206.21:88/Movie/GetMoviesByGenre?device=4&genreid=' + str(item["ID"]) + '&start=0&length=25', 11, '', '25', str(item["ID"]), 0)
	if 'GetMoviesByGenre' in url:
		content = make_request(url)
		result = json.loads(content)
		for item in result:
			add_link('', item["Title"], 0, 'http://117.103.206.21:88/Movie/GetMovieStream?device=4&path=' + item["MovieUrls"][0]["Path"].replace('SD', 'HD'), item["Thumbnail3"], item["SummaryShort"])
		add_dir('Next', 'http://117.103.206.21:88/Movie/GetMoviesByGenre?device=4&genreid=' + type + '&start=' + str(int(query)+page) + '&length=' + str(query), 11, '', str(int(query)+page), type, page)
	
def get_vtc(url = None):
	content = make_request(url)
	
	result = json.loads(content)
	for item in result:
		path = item["ChannelUrls"][0]["Path"]
		if 'http' in path:
			add_link('', item["Name"], 0, item["ChannelUrls"][0]["Path"], item["Thumbnail2"], '')
		else:
			add_link('', item["Name"], 0, "http://117.103.206.21:88/channel/GetChannelStream?device=4&path=" + item["ChannelUrls"][0]["Path"], item["Thumbnail2"], '')

def get_hdonline(url = None):
	if url == '':
		content = make_request('http://hdonline.vn/')
		soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
		items = soup.find('div',{'id' : 'full-mn-phim-le'}).findAll('a')
		for item in items:
			href = item.get('href')
			if href is not None:
				try:
					add_dir(item.text, href, 13, thumbnails + 'HDOnline.png', query, type, 0)
				except:
					pass
		return
	if 'xem-phim' in url:	
		content = make_request(url)
		soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
		items = soup.findAll('ul', {'class' : 'clearfix listmovie'})[1].findAll('li')
		for item in items:
			a = item.find('a')
			img = item.find('img')
			span = item.find('span',{'class' : 'type'})
			href = a.get('href')
			if href is not None:
				try:
					if span is not None:
						add_dir(a.get('title') + ' (' + span.text + ')', href, 9, a.img['src'], '', '', 0)
					else:	
						add_link('', a.get('title'), 0, href, img['src'], '')
				except:
					pass
		items = soup.find('div',{'class' : 'pagination pagination-right'})
		if items is not None:
			for item in items.findAll('a'):
				a = item
				href = a.get('href')
				if href is not None:
					try:
						add_dir(a.get('title'), href, 9, thumbnails + 'zui.png', '', '', 0)
					except:
						pass
		
def get_zui(url = None):
	if url == '':
		content = make_request('http://zui.vn')
		soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
		items = soup.find('div',{'class' : 'span8 visible-desktop visible-tablet'}).findAll('a')
		for item in items:
			href = item.get('href')
			if href is not None:
				try:
					add_dir(item.text, href, 9, thumbnails + 'zui.png', query, type, 0)
				except:
					pass
		return
	if 'the-loai' in url or 'phim-' in url:	
		content = make_request(url)
		soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
		groups = soup.find('ul', {'class' : 'group'})
		if groups is not None:
			for item in groups.findAll('a'):
				matchObj = re.match( r'change_group_chapter\((\d+),(\d+),(\d+)\)', item['onclick'], re.M|re.I)
				response = urlfetch.fetch(
			url = 'http://zui.vn/?site=movie&view=show_group_chapter',
			method ='POST',
			data = {
				"pos": matchObj.group(1),
				"movie_id": matchObj.group(2),
				"type": matchObj.group(3)
			}
		)
				soup = BeautifulSoup(str(response.content), convertEntities=BeautifulSoup.HTML_ENTITIES)
				for item in soup.findAll('a'):
					add_link('', u'Tập ' + item.text, 0, 'http://zui.vn/' + item['href'], thumbnails + 'zui.png', '')
		else:
			items = soup.find('ul',{'class' : 'movie_chapter'})
			if items is not None:
				for item in items.findAll('a'):
					a = item
					href = a.get('href')
					if href is not None:
						try:
							add_link('', u'Tập ' + a.text, 0, 'http://zui.vn/' + href, thumbnails + 'zui.png', '')
							#add_dir(u'Tập ' + a.text, 'http://zui.vn/' + href, 9, thumbnails + 'zui.png', '', '', 0)
						except:
							pass
			else:
				items = soup.findAll('div',{'class' : 'poster'})
				for item in items:
					a = item.find('a')
					span = item.find('span',{'class' : 'type'})
					href = a.get('href')
					if href is not None:
						try:
							if span is not None:
								add_dir(a.get('title') + ' (' + span.text + ')', href, 9, a.img['src'], '', '', 0)
							else:	
								add_link('', a.get('title'), 0, href, a.img['src'], '')
						except:
							pass
				items = soup.find('div',{'class' : 'pagination pagination-right'})
				if items is not None:
					for item in items.findAll('a'):
						a = item
						href = a.get('href')
						if href is not None:
							try:
								add_dir(a.get('title'), href, 9, thumbnails + 'zui.png', '', '', 0)
							except:
								pass
	else:
		content = make_request(url)
		soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
		groups = soup.find('ul', {'class' : 'group'})
		if groups is not None:
			for item in groups.findAll('a'):
				matchObj = re.match( r'change_group_chapter\((\d+),(\d+),(\d+)\)', item['onclick'], re.M|re.I)
				response = urlfetch.fetch(
			url = 'http://zui.vn/?site=movie&view=show_group_chapter',
			method ='POST',
			data = {
				"pos": matchObj.group(1),
				"movie_id": matchObj.group(2),
				"type": matchObj.group(3)
			}
		)
				soup = BeautifulSoup(str(response.content), convertEntities=BeautifulSoup.HTML_ENTITIES)
				for item in soup.findAll('a'):
					add_link('', u'Tập ' + item.text, 0, 'http://zui.vn/' + item['href'], thumbnails + 'zui.png', '')
			return
	
		items = soup.find('ul',{'class' : 'movie_chapter'})
		if items is not None:
			for item in items.findAll('a'):
				a = item
				href = a.get('href')
				if href is not None:
					try:
						add_link('', u'Tập ' + a.text, 0, 'http://zui.vn/' + href, thumbnails + 'zui.png', '')
						#add_dir(u'Tập ' + a.text, 'http://zui.vn/' + href, 9, thumbnails + 'zui.png', '', '', 0)
					except:
						pass
	
def get_fpt_other(url):
	content = make_request(url)
	soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
	items = soup.findAll('a')
	for item in items:
		href = item.get('href')
		if href is not None and 'the-loai-more' in href and 'Xem' not in item.text:
			try:
				add_dir(item.text, 'http://play.fpt.vn' + href, 8, thumbnails + 'fptplay.jpg', query, type, 0)
			except:
				pass

def get_fpt_tvshow_cat(url):
	content = make_request(url)
	soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
	if url is not None and '/Video/' not in url:
		items = soup.findAll('div', {'class' : 'col'})
		for item in items:
			img = item.a.img['src']
			href = item.a['href']
			text = item.a.img['alt']	
			try:
				add_dir(text, 'http://play.fpt.vn' + href, 8, img, '', '', 0)
			except:
				pass

	items = soup.find('ul', {'class' : 'pagination pagination-sm'}).findAll('a')
	for item in items:
		href = ''
		href = item.get('href')
		if href is not None and 'the-loai-more' in href and 'Xem' not in item.text:
			try:
				add_dir('Trang ' + item.text, 'http://play.fpt.vn' + href, 8, thumbnails + 'fptplay.jpg', query, type, 0)
			except:
				pass
		if href is not None and '/Video/' in href:
			try:
				add_link('', u'Tập ' + item.text, 0, 'http://play.fpt.vn' + href, thumbnails + 'fptplay.jpg', '')
			except:
				pass
		
def get_htv():
	content = make_request('http://www.htvonline.com.vn/livetv')
	soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
	items = soup.findAll('a', {'class' : 'mh-grids5-img'})
	for item in items:
		img = item.find('img')
		if img is not None:
			try:
				add_link('', item['title'], 0, item['href'], img['src'], '')
			except:
				pass

#def get_sctv(url):
	content = make_request('http://tv24.vn/LiveTV/Tivi_Truc_Tuyen_SCTV_VTV_HTV_THVL_HBO_STARMOVIES_VTC_VOV_BongDa_Thethao_Hai_ThoiTrang_Phim_PhimHongKong.html')
	soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
	items = soup.findAll('a')
	for item in items:
		img = item.find('img')
		if img is not None and 'LiveTV' in item['href']:
			try:
				add_link('', item['href'], 0, 'http://tv24.vn' + item['href'], img['src'], '')
			except:
				pass
		
def get_categories():
	add_link('', '[COLOR lime]********TH ONETV (cho mạng FPT) *******[/COLOR]', 0, '', thumbnails + '', '')
	add_link('', 'K+1 HD', 0, 'udp://@225.1.1.134:30120', thumbnails + '', '')
	add_link('', 'K+NS HD', 0, 'udp://@225.1.1.45:30120', thumbnails + '', '')
	add_link('', 'K+PC HD', 0, 'udp://@225.1.1.47:30120', thumbnails + '', '')
	add_link('', 'K+PM HD', 0, 'udp://@225.1.1.46:30120', thumbnails + '', '')
	add_link('', 'BÓNG ĐÁ TV HD', 0, 'udp://@225.1.2.243:30120', thumbnails + 'Cab16-BongdaHD.jpg', '')
        add_link('', 'THỂ THAO TV HD ', 0, 'udp://@225.1.2.241:30120', thumbnails + 'TheThaoTVHD.jpg', '')
	add_link('', 'VTV1 HD', 0, 'udp://@225.1.2.248:30120', thumbnails + 'VTV1 HD.jpg', '')
	add_link('', 'VTV3 HD', 0, 'udp://@225.1.2.247:30120', thumbnails + 'VTV3 HD.jpg', '')
        add_link('', 'VTV6 HD', 0, 'udp://@225.1.2.245:30120', thumbnails + 'VTV6 HD.jpg', '')
        add_link('', 'QPVN HD', 0, 'udp://@225.1.2.217:30120', thumbnails + '', '')
	add_link('', 'QUỐC HỘI HD', 0, 'udp://@225.1.2.148:30120', thumbnails + '', '')
	add_link('', 'VTC HD1', 0, 'udp://@225.1.2.254:30120', thumbnails + 'VTC HD1.jpg', '')
        add_link('', 'VTC HD2', 0, 'udp://@225.1.2.253:30120', thumbnails + 'VTC HD2.jpg', '')
        add_link('', 'VTC HD3', 0, 'udp://@225.1.2.252:30120', thumbnails + 'VTC-HD3.jpg', '')
        add_link('', 'VTC3 HD', 0, 'udp://@225.1.2.251:30120', '', '')
	add_link('', 'VTC4 HD', 0, 'udp://@225.1.2.200:30120', '', '')
        add_link('', 'ITV HD', 0, 'udp://@225.1.2.250:30120', thumbnails + 'ITV HD.jpg', '')
        add_link('', 'HTV2 HD', 0, 'udp://@225.1.1.193:30120', thumbnails + 'HTV2 HD.jpg', '')
        add_link('', 'HTV7 HD', 0, 'udp://@225.1.1.192:30120', thumbnails + 'HTV7 HD.jpg', '')
        add_link('', 'HTV9 HD', 0, 'udp://@225.1.1.190:30120', thumbnails + 'HTV9 HD.jpg', '')
        add_link('', 'HTVC THUẦN VIỆT HD', 0, 'udp://@225.1.1.186:30120', thumbnails + 'ThuanViet HD.jpg', '')
        add_link('', 'HTVC PHIM HD', 0, 'udp://@225.1.1.184:30120', thumbnails + 'HTVC MOVIE HD.jpg', '')
	add_link('', 'HTVC FBNC HD', 0, 'udp://@225.1.1.182:30120', thumbnails + 'FBNC.jpg', '')
	add_link('', 'AXN HD', 0, 'udp://@225.1.2.225:30120', thumbnails + 'AXN HD.jpg', '')
        add_link('', 'STARMOVIES HD', 0, 'udp://@225.1.2.239:30120', thumbnails + 'StarMoviesHD.jpg', '')
        add_link('', 'HBO HD', 0, 'udp://@225.1.2.233:30120', thumbnails + 'HBO-HD.png', '')
	add_link('', 'CARTOON NETWORK HD', 0, 'udp://@225.1.2.231:30120', thumbnails + '', '')
        add_link('', 'NATGEO HD', 0, 'udp://@225.1.2.235:30120', thumbnails + '', '')
	add_link('', 'DISCOVERY WORLD HD ', 0, 'udp://@225.1.2.223:30120', thumbnails + 'discovery hd.jpg', '')
	add_link('', 'CHANNEL OUTDOOR HD', 0, 'udp://@225.1.2.215:30120', thumbnails + '', '')
        add_link('', 'STAR WORLD HD', 0, 'udp://@225.1.2.237:30120', thumbnails + '', '')
	add_link('', 'FOX SPORTS PLUS HD', 0, 'udp://@225.1.2.229:30120', thumbnails + 'fox_sports_hd.jpg', '')
	add_link('', 'FASHIONTV HD', 0, 'udp://@225.1.2.227:30120', thumbnails + '', '')
	add_link('', 'CHANNEL V HD', 0, 'udp://@225.1.1.188:30120', thumbnails + '', '')
	add_link('', 'VTVCAB1', 0, 'udp://@225.1.2.150:30120', thumbnails + '', '')
        add_link('', 'VTVCAB2', 0, 'udp://@225.1.2.159:30120', thumbnails + '', '')
        add_link('', 'VTVCAB3', 0, 'udp://@225.1.2.158:30120', thumbnails + '', '')
        add_link('', 'VTVCAB4', 0, 'udp://@225.1.2.153:30120', thumbnails + '', '')
        add_link('', 'VTVCAB5', 0, 'udp://@225.1.2.156:30120', thumbnails + '', '')
        add_link('', 'VTVCAB6', 0, 'udp://@225.1.1.254:30120', thumbnails + '', '')
        add_link('', 'VTVCAB7', 0, 'udp://@225.1.2.157:30120', thumbnails + '', '')
        add_link('', 'VTVCAB8', 0, 'udp://@225.1.2.161:30120', thumbnails + '', '')
        add_link('', 'VTVCAB9', 0, 'udp://@225.1.2.154:30120', thumbnails + '', '')
        add_link('', 'VTVCAB10', 0, 'udp://@225.1.2.152:30120', thumbnails + '', '')
        add_link('', 'VTVCAB11', 0, 'udp://@225.1.1.252:30120', thumbnails + '', '')
        add_link('', 'VTVCAB12', 0, 'udp://@225.1.2.155:30120', thumbnails + '', '')
        add_link('', 'VTVCAB14', 0, 'udp://@225.1.1.253:30120', thumbnails + '', '')
        add_link('', 'VTVCAB15', 0, 'udp://@225.1.1.251:30120', thumbnails + '', '')
        add_link('', 'VTVCAB16', 0, 'udp://@225.1.2.160:30120', thumbnails + '', '')
        add_link('', 'VTVCAB17', 0, 'udp://@225.1.2.151:30120', thumbnails + '', '')
	add_link('', 'VTVCAB20', 0, 'udp://@225.1.1.15:30120', thumbnails + '', '')
	add_link('', 'K+1', 0, 'udp://@225.1.1.48:30120', thumbnails + '', '')
	add_link('', 'K+NS', 0, 'udp://@225.1.1.142:30120', thumbnails + '', '')
	add_link('', 'K+PC', 0, 'udp://@225.1.1.139:30120', thumbnails + '', '')
	add_link('', 'K+PM', 0, 'udp://@225.1.1.140:30120', thumbnails + '', '')
        add_link('', 'MOV Hanoicab', 0, 'udp://@225.1.1.206:30120', thumbnails + '', '')
        add_link('', 'HITV Hanoicab', 0, 'udp://@225.1.1.209:30120', thumbnails + '', '')
        add_link('', 'VNK Hanoicab', 0, 'udp://@225.1.2.93:30120', thumbnails + '', '')
        add_link('', 'You Hanoicab', 0, 'udp://@225.1.1.207:30120', thumbnails + '', '')
        add_link('', 'An vien ANTG', 0, 'udp://@225.1.1.208:30120', thumbnails + '', '')
	add_link('', 'An vien PHIM HAY', 0, 'udp://@225.1.1.222:30120', thumbnails + '', '')
	add_link('', 'An vien NCM', 0, 'udp://@225.1.1.225:30120', thumbnails + '', '')
	add_link('', 'An vien Miền tây', 0, 'udp://@225.1.1.221:30120', thumbnails + '', '')
	add_link('', 'An vien Vietteen', 0, 'udp://@225.1.1.223:30120', thumbnails + '', '')
	add_link('', 'An vien SAM', 0, 'udp://@225.1.1.224:30120', thumbnails + '', '')
	add_link('', 'NATGEO', 0, 'udp://@225.1.1.244:30120', thumbnails + '', '')
        add_link('', 'DISCOVEY', 0, 'udp://@225.1.1.238:30120', thumbnails + '', '')
        add_link('', 'TLC', 0, 'udp://@225.1.1.236:30120', thumbnails + '', '')
        add_link('', 'ANIMAL PLANET', 0, 'udp://@225.1.1.231:30120', thumbnails + '', '')
        add_link('', 'DA VINCI', 0, 'udp://@225.1.1.197:30120', thumbnails + '', '')
		
	add_link('', '[COLOR lime]******************* TH SCTV**************************[/COLOR]', 0, '', thumbnails + '', '')
	add_link('', 'SCTVHD SÓNG NHẠC', 0, 'rtmpe://112.197.2.135/glive/C006_HD_4 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTVHD DU LỊCH', 0, 'rtmpe://112.197.2.135/glive/C007_HD_4 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTVHD PHIM VIỆT', 0, 'rtmpe://112.197.2.135/glive/C009_HD_4 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTVHD PHIM CHÂU Á', 0, 'rtmpe://112.197.2.135/glive/C010_HD_4 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTVHD HÀI', 0, 'rtmpe://112.197.2.135/glive/C011_HD_4 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTVHD SÂN KHẤU', 0, 'rtmpe://112.197.2.135/glive/C012_HD_4 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTVHD PHIM TỔNG HỢP', 0, 'rtmpe://112.197.2.135/glive/C013_HD_4 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTVHD GIẢI TRÍ TỔNG HỢP', 0, 'rtmpe://112.197.2.135/glive/C014_HD_2 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTVHD PHIM NƯỚC NGOÀI ĐẶC SẮC', 0, 'rtmpe://112.197.2.135/glive/C015_HD_2 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTVHD THIẾU NHI', 0, 'rtmpe://112.197.2.135/glive/C016_HD_2 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTVHD PHỤ NỮ VÀ GIA ĐÌNH', 0, 'rtmpe://112.197.2.135/glive/C017_HD_2 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTVHD THE THAO', 0, 'rtmpe://112.197.2.135/glive/C008_HD_4 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTV15 HD', 0, 'rtmpe://112.197.2.135/glive/C042_SD_3 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTVHD STAR MOVIES', 0, 'rtmpe://112.197.2.135/glive/C001_HD_4 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTV1', 0, 'rtmpe://112.197.2.154:1935/live2/sctv1_2 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTV2', 0, 'rtmpe://112.197.2.154:1935/live2/sctv2_2 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTV3', 0, 'rtmpe://112.197.2.154:1935/live2/sctv3_2 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTV4', 0, 'rtmpe://112.197.2.154:1935/live2/sctv4_2 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTV5', 0, 'rtmpe://112.197.2.154:1935/live2/sctv5_2 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTV6', 0, 'rtmpe://112.197.2.154:1935/live2/sctv6_2 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTV7', 0, 'rtmpe://112.197.2.154:1935/live2/sctv7_2 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTV8', 0, 'rtmpe://112.197.2.154:1935/live2/sctv8_2 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTV9', 0, 'rtmpe://112.197.2.154:1935/live2/sctv9_2 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTV10', 0, 'rtmpe://112.197.2.154:1935/live2/sctv10_2 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTV11', 0, 'rtmpe://112.197.2.154:1935/live2/sctv11_2 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTV12', 0, 'rtmpe://112.197.2.154:1935/live2/sctv12_2 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTV13', 0, 'rtmpe://112.197.2.154:1935/live2/sctv13_2 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTV14', 0, 'rtmpe://112.197.2.154:1935/live2/sctv14_2 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTV15', 0, 'rtmpe://112.197.2.135/glive/C042_SD_2 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTV16', 0, 'rtmpe://112.197.2.154:1935/live2/sctv16_2 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTV17', 0, 'rtmpe://112.197.2.154:1935/live2/sctv17_2 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')
	add_link('', 'SCTV18', 0, 'rtmpe://112.197.2.135/glive/C008_HD_2 live=1 swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://www.tv24.vn/ token=qrtkL6xTjSqeG4q3', thumbnails + '', '')

	add_link('', '[COLOR lime]*********************TH VTVPLay ***************************[/COLOR]', 0, '', thumbnails + '', '')
	add_link('', 'VTV1', 0, 'http://vtv.live.cdn.fptplay.net/vtvlive/smil:vtv1sd_hls.smil/playlist.m3u8', thumbnails + 'VTV1.jpg', '')
	add_link('', 'VTV3', 0, 'http://vtv.live.cdn.fptplay.net/vtvlive/smil:vtv3sd_hls.smil/playlist.m3u8', thumbnails + 'VTV3 HD.jpg', '')
	add_link('', 'VTV6', 0, 'http://vtv.live.cdn.fptplay.net/vtvlive/smil:vtv6sd_hls.smil/playlist.m3u8', thumbnails + 'VTV6 HD.jpg', '')
	add_link('', 'VTVCAB1', 0, 'http://vtv.live.cdn.fptplay.net/vtvlive/smil:giaitritv_hls.smil/playlist.m3u8', thumbnails + '', '')
	add_link('', 'VTVCAB2', 0, 'http://vtv.live.cdn.fptplay.net/vtvlive/smil:phimviet_hls.smil/playlist.m3u8', thumbnails + '', '')
        add_link('', 'VTVCAB3 THETHAOTV', 0, 'http://vtv.live.cdn.fptplay.net/vtvlive/smil:thethaotvsd_hls.smil/playlist.m3u8', thumbnails + '', '')
        add_link('', 'VTVCAB4', 0, 'http://vtv.live.cdn.fptplay.net/vtvlive/smil:kenh17_hls.smil/playlist.m3u8', thumbnails + '', '')
	add_link('', 'VTVCAB5', 0, 'http://vtv.live.cdn.fptplay.net/vtvlive/smil:echanel_hls.smil/playlist.m3u8', thumbnails + '', '')
	add_link('', 'VTVCAB6', 0, 'http://vtv.live.cdn.fptplay.net/vtvlive/smil:haytv_hls.smil/chunklist_b1200000.m3u8', thumbnails + '', '')
	add_link('', 'VTVCAB7', 0, 'http://vtv.live.cdn.fptplay.net/vtvlive/smil:ddramas_hls.smil/playlist.m3u8', thumbnails + '', '')
	add_link('', 'VTVCAB8', 0, 'http://vtv.live.cdn.fptplay.net/vtvlive/smil:bibi_hls.smil/playlist.m3u8', thumbnails + '', '')
	add_link('', 'VTVCAB9', 0, 'http://vtv.live.cdn.fptplay.net/vtvlive/smil:infotv_hls.smil/playlist.m3u8', thumbnails + '', '')
	add_link('', 'VTVCAB10', 0, 'http://vtv.live.cdn.fptplay.net/vtvlive/smil:o2tv_hls.smil/playlist.m3u8', thumbnails + '', '')
	add_link('', 'VTVCAB12', 0, 'http://vtv.live.cdn.fptplay.net/vtvlive/smil:styletv_hls.smil/playlist.m3u8', thumbnails + '', '')
	add_link('', 'VTVCAB15', 0, 'http://vtv.live.cdn.fptplay.net/vtvlive/smil:investtv_hls.smil/playlist.m3u8', thumbnails + '', '')
	add_link('', 'VTVCAB16 BONGDATV', 0, 'http://vtv.live.cdn.fptplay.net/vtvlive/smil:bongdatvsd_hls.smil/playlist.m3u8', thumbnails + '', '')
	add_link('', 'VTVCAB17', 0, 'http://vtv.live.cdn.fptplay.net/vtvlive/smil:yeah1tv_hls.smil/playlist.m3u8', thumbnails + '', '')
        add_link('', 'HTV9', 0, 'http://vtv.live.cdn.fptplay.net/vtvlive/smil:htv9_hls.smil/playlist.m3u8', thumbnails + '', '')
	add_link('', 'SCTVHD HAI(720P)', 0, 'http://vtv.live.cdn.fptplay.net/vtvlive/smil:sctvhaihd_hls.smil/playlist.m3u8', thumbnails + '', '')
	add_link('', 'ARIANG', 0, 'http://vtv.live.cdn.fptplay.net/vtvlive/smil:arirang_hls.smil/playlist.m3u8', thumbnails + '', '')
	add_link('', 'KBS', 0, 'http://vtv.live.cdn.fptplay.net/vtvlive/smil:kbs_hls.smil/playlist.m3u8', thumbnails + '', '')

	#add_link('', 'HBO HD', 0, '', '', '')
	#http://scache.fptplay.net.vn/live/htvcplusHD_1000.stream/manifest.f4m
	#add_dir('HTVOnline', url, 5, thumbnails + 'htv.jpg', query, type, 0)
	#add_dir('SCTV', url, 12, thumbnails + 'SCTV.png', query, type, 0)
	#add_dir('VTCPlay - TV', 'http://117.103.206.21:88/Channel/GetChannels?device=4', 10, thumbnails + 'vtcplay.jpg', query, type, 0)
	#add_dir('VTCPlay - Movies', '', 11, thumbnails + 'vtcplay.jpg', query, type, 0)
	#add_dir('FPTPlay - TV', url, 6, thumbnails + 'fptplay_logo.jpg', query, type, 0)
	#add_dir('FPTPlay - TVShow', url, 7, thumbnails + 'fptplay_logo.jpg', query, type, 0)
	#add_dir('ZUI.VN', url, 9, thumbnails + 'zui.png', query, type, 0)
	#add_dir('HDOnline.vn', url, 13, thumbnails + 'HDOnline.png', query, type, 0)

def searchMenu(url, query = '', type='f', page=0):
	add_dir('New Search', url, 2, icon, query, type, 0)
	add_dir('Clear Search', url, 3, icon, query, type, 0)

	searchList=cache.get('searchList').split("\n")
	for item in searchList:
		add_dir(item, url, 2, icon, item, type, 0)

def resolve_url(url):
	if 'zui.vn' in url:
		headers2 = {'User-agent' : 'iOS / Chrome 32: Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) CriOS/32.0.1700.20 Mobile/11B554a Safari/9537.53',
											 'Referer' : 'http://www.google.com'}
		content = make_request(url, headers2)
		soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
		for line in content.splitlines():
			s = line.strip()
			if s.startswith('movie_play_chapter'):
				#movie_play_chapter('mediaplayer', '1', 'rtmp://103.28.37.89:1935/vod3/mp4:/phimle/Vikingdom.2013.720p.WEB-DL.H264-PHD.mp4', '/uploads/movie_view/5c65563b1ce8d106c013.jpg', 'http://zui.vn/subtitle/Vikingdom.2013.720p.WEB-DL.H264-PHD.srt');
				matchObj = re.match( r'[^\']*\'([^\']*)\', \'([^\']*)\', \'([^\']*)\', \'([^\']*)\', \'([^\']*)\'', s, re.M|re.I)
				url = matchObj.group(3)
				url = url.replace(' ','%20')
				xbmc.Player().play(url)
				xbmc.Player().setSubtitles(matchObj.group(5))
				return
				break

	if 'play.fpt.vn/Video' in url:
		content = make_request(url)
		soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
		for line in content.splitlines():
			s = line.strip()
			if s.startswith('"<source src='):
				start = s.index('\'')+1
				end = s.index('\'', start+1)
				url = s[start:end]
				break

	if 'play.fpt.vn' in url:
		content = make_request(url)
		soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
		item = soup.find('div', {'id' : 'bitrate-tag'})
		url = item['highbitrate-link']
		content = make_request(url)
		for line in content.splitlines():
			s = line.strip()
			if s.startswith('<id>'):
				start = s.index('<id>')+4
				end = s.index('<', start+1)
				url = url.replace('manifest.f4m',s[start:end])
				url = 'http://scache.fptplay.net.vn/live/' + s[start:end] + '/playlist.m3u8'
				break

	if 'htvonline' in url:
		content = make_request(url)
		for line in content.splitlines():
			if line.strip().startswith('file: '):
				url = line.strip().replace('file: ', '').replace('"', '').replace(',', '')
				break

	#if 'tv24' in url:
		content = make_request(url)
		for line in content.splitlines():
			if line.strip().startswith('\'file\': \'http'):
				url = line.strip().replace('\'file\': ', '').replace('\'', '').replace(',', '')
				break
		
	if 'GetChannelStream' in url or 'GetMovieStream' in url or 'vtvplay' in url:
		content = make_request(url)
		url = content.replace("\"", "")
		url = url[:-5]
	item = xbmcgui.ListItem(path=url)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
	return

def add_link(date, name, duration, href, thumb, desc):
	description = date+'\n\n'+desc
	u=sys.argv[0]+"?url="+urllib.quote_plus(href)+"&mode=4"
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=thumb)
	liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description, "Duration": duration})
	if 'zui' in href:
		liz.setProperty('IsPlayable', 'false')
	else:
		liz.setProperty('IsPlayable', 'true')
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)



def add_dir(name,url,mode,iconimage,query='',type='f',page=0):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&query="+str(query)+"&type="+str(type)+"&page="+str(page)#+"&name="+urllib.quote_plus(name)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	return ok


def get_params():
	param=[]
	paramstring=sys.argv[2]
	if len(paramstring)>=2:
			params=sys.argv[2]
			cleanedparams=params.replace('?','')
			if (params[len(params)-1]=='/'):
					params=params[0:len(params)-2]
			pairsofparams=cleanedparams.split('&')
			param={}
			for i in range(len(pairsofparams)):
					splitparams={}
					splitparams=pairsofparams[i].split('=')
					if (len(splitparams))==2:
							param[splitparams[0]]=splitparams[1]

	return param

xbmcplugin.setContent(int(sys.argv[1]), 'movies')

params=get_params()

url=''
name=None
mode=None
query=None
type='f'
page=0

try:
	type=urllib.unquote_plus(params["type"])
except:
	pass
try:
	page=int(urllib.unquote_plus(params["page"]))
except:
	pass
try:
	query=urllib.unquote_plus(params["query"])
except:
	pass
try:
	url=urllib.unquote_plus(params["url"])
except:
	pass
try:
	name=urllib.unquote_plus(params["name"])
except:
	pass
try:
	mode=int(params["mode"])
except:
	pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "type: "+str(type)
print "page: "+str(page)
print "query: "+str(query)

if mode==None:
	get_categories()
#		fslink_get_video_categories(FSLINK+'/phim-anh.html')

elif mode==1:
	searchMenu(url, '', type, page)

elif mode==2:
	search(url, query, type, page)

elif mode==3:
	clearSearch()

elif mode==4:
	resolve_url(url)
elif mode==5:
	get_htv()
elif mode==6:
	get_fpt()
elif mode==7:
	get_fpt_other('http://play.fpt.vn/the-loai/tvshow')
	#get_fpt_other('http://play.fpt.vn/the-loai/sport')
	#get_fpt_other('http://play.fpt.vn/the-loai/music')
	#get_fpt_other('http://play.fpt.vn/the-loai/general')
elif mode==8:
	get_fpt_tvshow_cat(url)
elif mode==9:
	get_zui(url)
elif mode==10:
	get_vtc(url)
elif mode==11:
	get_vtc_movies(url, query, type, page)
#elif mode==12:
	get_sctv(url)
elif mode==13:
	get_hdonline(url)
	 
xbmcplugin.endOfDirectory(int(sys.argv[1]))