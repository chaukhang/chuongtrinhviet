#!/usr/bin/python
#coding=utf-8
import xbmc,xbmcaddon,xbmcplugin,xbmcgui,sys,urllib,urllib2,re,os,codecs,unicodedata,base64
import simplejson as json

addonID = 'plugin.video.livetv'
addon = xbmcaddon.Addon(addonID)
pluginhandle = int(sys.argv[1])
home = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('path') ).decode("utf-8")
logos = xbmc.translatePath(os.path.join(home,"logos\\"))
dataPath = xbmc.translatePath(os.path.join(home, 'resources'))



def TVChannel(url):
    xmlcontent = GetUrl(url)
    names = re.compile('<name>(.+?)</name>').findall(xmlcontent)
    if len(names) == 1:
        items = re.compile('<item>(.+?)</item>').findall(xmlcontent)
        for item in items:
            thumb=""
            title=""
            link=""
            if "/title" in item:
                title = re.compile('<title>(.+?)</title>').findall(item)[0]
            if "/link" in item:
                link = re.compile('<link>(.+?)</link>').findall(item)[0]            
            if "/thumbnail" in item:
                thumb = re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            if "viettv24free" in link:                   
                link = re.compile('<link>(.+?)</link>').findall(item)[0] #required but not mean anything
            if "redirecttofptplay" in link:                   
                link = re.compile('<link>(.+?)</link>').findall(item)[0] #required but not mean anything
            if "redirecttohtvplus" in link:                   
                link = re.compile('<link>(.+?)</link>').findall(item)[0]    
            if ("redirecttoyoutube" in link) or ("redirecttodailymotion" in link):                   
                link = re.compile('<link>(.+?)</link>').findall(item)[0] #required but not mean anything
            if ("tosportsdevil" in link) or ("tovdubt" in link):                   
                link = re.compile('<link>(.+?)</link>').findall(item)[0]
            if ("redirecttomovieshd" in link) or ("toyeuphim" in link) or ("redirecttonetmovie" in link) or \
               ("redirectto1channel" in link) or ("redirecttokenh108" in link) or ("redirecttokenh88" in link) or \
               ("redirecttomoviebox" in link) or ("redirecttophimvang" in link) or ("redirecttoxomgiaitri" in link) or \
               ("redirecttoxixam" in link) or ("redirecttovkool" in link) or ("tomovienight" in link) or ("toyify" in link) or \
               ("tomovieshd2" in link) or ("tocartoons8" in link) or ("tokiddiecartoons" in link) or ("tonavix" in link) or \
               ("toxmovies8" in link) or ("togenesis" in link) or ("tophoenix" in link) or ("toanhtrang" in link) or \
               ("tophim14" in link) or ("tofootball" in link) or ("toxemphimso" in link) or ("toenter" in link) or \
               ("toitv" in link) or ("tofilmon1" in link) or ("tofilmon2" in link): 
                link = re.compile('<link>(.+?)</link>').findall(item)[0]            
            add_Link(title, link, thumb)
        xbmc.executebuiltin('Container.SetViewMode(52)')		
    else:
        for name in names:
            addDir('' + name + '', url+"?n="+name, 'index', '')
        xbmc.executebuiltin('Container.SetViewMode(52)')
		
def Channel():
    content = Get_Url(DecryptData(homeurl))
    match=re.compile("<title>([^<]*)<\/title>\s*<link>([^<]+)<\/link>\s*<thumbnail>(.+?)</thumbnail>").findall(content)	
    for title,url,thumbnail in match:
		addDir(title,url,'tvchannel',thumbnail)	
    xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)	

	
def resolveUrl(url):
	if 'xemphimso' in url:
		content = Get_Url(url)	
		url = urllib.unquote_plus(re.compile("file=(.+?)&").findall(content)[0])
	elif 'vtvplay' in url:
		content = Get_Url(url)
		url = content.replace("\"", "")
		url = url[:-5]
	elif 'vtvplus' in url:
		content = Get_Url(url)
		url = re.compile('var responseText = "(.+?)";').findall(content)[0]		
	elif 'htvonline' in url:
		content = Get_Url(url)	
		url = re.compile('data\-source=\"([^\"]*)\"').findall(content)[0]
	elif 'hplus' in url:
		content = Get_Url(url)	
		url = re.compile('iosUrl = "(.+?)";').findall(content)[0]		
	else:
		url = url
	item=xbmcgui.ListItem(path=url)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)	  
	return	

def Get_M3U(url,iconimage):
  m3ucontent = Get_Url(url)
  match = re.compile('#EXTINF:-?\d,(.+?)\n(.+)').findall(m3ucontent)
  for name,url in match:
	  add_Link(name.replace('TVSHOW - ','').replace('MUSIC - ',''),url,iconimage)
	  
def Index(url,iconimage):
    byname = url.split("?n=")[1]
    url = url.split("?")[0]
    xmlcontent = GetUrl(url)
    channels = re.compile('<channel>(.+?)</channel>').findall(xmlcontent)
    for channel in channels:
        if byname in channel:
            items = re.compile('<item>(.+?)</item>').findall(channel)
            for item in items:
                thumb=""
                title=""
                link=""
                if "/title" in item:
                    title = re.compile('<title>(.+?)</title>').findall(item)[0]
                if "/link" in item:
                    link = re.compile('<link>(.+?)</link>').findall(item)[0]
                if "/thumbnail" in item:
                    thumb = re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                if "youtube" in link:					
                    addDir(title, link, 'episodes', thumb)
                #old version if ("youtube" in link) or ("redirecttomovieshd" in link) or ("redirecttonetmovie" in link) or \
                   #("redirectto1channel" in link) or ("redirecttokenh108" in link) or ("redirecttokenh88" in link) or \
                   #("redirecttomoviebox" in link) or ("redirecttophimvang" in link) or ("redirecttoxomgiaitri" in link) or \
                   #("redirecttoxixam" in link) or ("redirecttovkool" in link):                   
                    #addDir(title, link, 'episodes', thumb)
                else:					
                    addLink('' + title + '', link, 'play', thumb)
    skin_used = xbmc.getSkinDir()
    if skin_used == 'skin.xeebo':
        xbmc.executebuiltin('Container.SetViewMode(50)')
		
def IndexGroup(url):
    xmlcontent = GetUrl(url)
    names = re.compile('<name>(.+?)</name>').findall(xmlcontent)
    if len(names) == 1:
        items = re.compile('<item>(.+?)</item>').findall(xmlcontent)
        for item in items:
            thumb=""
            title=""
            link=""
            if "/title" in item:
                title = re.compile('<title>(.+?)</title>').findall(item)[0]
            if "/link" in item:
                link = re.compile('<link>(.+?)</link>').findall(item)[0]
            if "/thumbnail" in item:
                thumb = re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
            add_Link(title, link, thumb)
        skin_used = xbmc.getSkinDir()
        if skin_used == 'skin.xeebo':
            xbmc.executebuiltin('Container.SetViewMode(52)')
        else:
            xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)			
    else:
        for name in names:
            addDir('' + name + '', url+"?n="+name, 'index', '')

def Index_Group(url):
    xmlcontent = GetUrl(url)
    names = re.compile('<name>(.+?)</name>\s*<thumbnail>(.+?)</thumbnail>').findall(xmlcontent)
    if len(names) == 1:
        items = re.compile('<item>(.+?)</item>').findall(xmlcontent)
        for item in items:
            thumb=""
            title=""
            link=""
            if "/title" in item:
                title = re.compile('<title>(.+?)</title>').findall(item)[0]
            if "/link" in item:
                link = re.compile('<link>(.+?)</link>').findall(item)[0]
            if "/thumbnail" in item:
                thumb = re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]                      
            addLink(title, link, 'play', thumb)
        skin_used = xbmc.getSkinDir()
        if skin_used == 'skin.xeebo':
            xbmc.executebuiltin('Container.SetViewMode(50)')
    else:
        for name,thumb in names:
            addDir(name, url+"?n="+name, 'index', thumb)

def menulist(homepath):
  try:
    mainmenu=open(homepath, 'r')  
    link=mainmenu.read()
    mainmenu.close()
    match=re.compile("<title>([^<]*)<\/title>\s*<link>([^<]+)<\/link>\s*<thumbnail>(.+?)</thumbnail>").findall(link)
    return match
  except:
    pass
	
def PlayVideo(url,title):
    
        title = urllib.unquote_plus(title)
        playlist = xbmc.PlayList(1)
        playlist.clear()
        listitem = xbmcgui.ListItem(title)
        listitem.setInfo('video', {'Title': title})
        xbmcPlayer = xbmc.Player()
        playlist.add(url, listitem)
        xbmcPlayer.play(playlist)
		
def Get_Url(url):
    try:
		req=urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)')
		response=urllib2.urlopen(req)
		link=response.read()
		response.close()  
		return link
    except:
		pass
    
def GetUrl(url):
    link = ""
    if os.path.exists(url)==True:
        link = open(url).read()
    else:
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
    link = ''.join(link.splitlines()).replace('\'','"')
    link = link.replace('\n','')
    link = link.replace('\t','')
    link = re.sub('  +',' ',link)
    link = link.replace('> <','><')
    return link
	
def add_Link(name,url,iconimage):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode=stream"+"&iconimage="+urllib.quote_plus(iconimage)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    liz.setProperty('IsPlayable', 'true')
    if 'viettv24free' in url:
        u = 'plugin://plugin.video.viettv24'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttofptplay' in url:
        u = 'plugin://plugin.video.fptplay'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttohtvplus' in url:
        u = 'plugin://plugin.video.HTVonline'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttoyoutube' in url:
        u = 'plugin://plugin.video.youtube'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttodailymotion' in url:
        u = 'plugin://plugin.video.dailymotion_com'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tosportsdevil' in url:
        u = 'plugin://plugin.video.SportsDevil'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tovdubt' in url:
        u = 'plugin://plugin.video.vdubt'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttomovieshd' in url:
        u = 'plugin://plugin.video.giaitritv'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'toxmovies8' in url:
        u = 'plugin://plugin.video.xmovies8'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'togenesis' in url:
        u = 'plugin://plugin.video.genesis'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tomovieshd2' in url:
        u = 'plugin://plugin.video.movieshd'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok        
    if 'toyify' in url:
        u = 'plugin://plugin.video.yifymovies.hd'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tomovienight' in url:
        u = 'plugin://plugin.video.movienight'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tophoenix' in url:
        u = 'plugin://plugin.video.phstreams'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tocartoons8' in url:
        u = 'plugin://plugin.video.cartoons8'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tokiddiecartoons' in url:
        u = 'plugin://plugin.video.kiddiecartoons'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tonavix' in url:
        u = 'plugin://script.navi-x'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttonetmovie' in url:
        u = 'plugin://plugin.video.netmovie'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttonetmovie' in url:
        u = 'plugin://plugin.video.netmovie'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirectto1channel' in url:
        u = 'plugin://plugin.video.1channel'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttokenh108' in url:
        u = 'plugin://plugin.video.kenh108.com'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttokenh88' in url:
        u = 'plugin://plugin.video.kenh88'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttomoviebox' in url:
        u = 'plugin://plugin.video.moviebox'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttophimvang' in url:
        u = 'plugin://plugin.video.phimvang.org'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttoxomgiaitri' in url:
        u = 'plugin://plugin.video.xomgiaitri'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttoxixam' in url:
        u = 'plugin://plugin.video.phim.xixam.com'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttoxomgiaitri' in url:
        u = 'plugin://plugin.video.xomgiaitri'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'redirecttovkool' in url:
        u = 'plugin://plugin.video.vkool'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'toyeuphim' in url:
        u = 'plugin://plugin.video.yeuphim1'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'toanhtrang' in url:
        u = 'plugin://plugin.video.anhtrang.org'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tophim14' in url:
        u = 'plugin://plugin.video.phim14.net'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tofootball' in url:
        u = 'plugin://plugin.video.footballreplays'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'toxemphimso' in url:
        u = 'plugin://plugin.video.xemphimso'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'toenter' in url:
        u = 'plugin://plugin.video.allinone'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'toitv' in url:
        u = 'plugin://plugin.video.itvplus'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tofilmon1' in url:
        u = 'plugin://plugin.video.F.T.V'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'tofilmon2' in url:
        u = 'plugin://plugin.video.filmontv'  
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)  

def addLink(name,url,mode,iconimage):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
    return ok
	
def addDir(name,url,mode,iconimage):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    '''old version
    if 'redirecttomovieshd' in url:
        u = 'plugin://plugin.video.giaitritv'
    if 'redirecttonetmovie' in url:
        u = 'plugin://plugin.video.netmovie'
    if 'redirectto1channel' in url:
        u = 'plugin://plugin.video.1channel'
    if 'redirecttokenh108' in url:
        u = 'plugin://plugin.video.kenh108.com'
    if 'redirecttokenh88' in url:
        u = 'plugin://plugin.video.kenh88'
    if 'redirecttomoviebox' in url:
        u = 'plugin://plugin.video.moviebox'
    if 'redirecttophimvang' in url:
        u = 'plugin://plugin.video.phimvang.org'
    if 'redirecttoxomgiaitri' in url:
        u = 'plugin://plugin.video.xomgiaitri'
    if 'redirecttoxixam' in url:
        u = 'plugin://plugin.video.phim.xixam.com'
    if 'redirecttoxomgiaitri' in url:
        u = 'plugin://plugin.video.xomgiaitri'
    if 'redirecttovkool' in url:
        u = 'plugin://plugin.video.vkool'
    '''
    if ('www.youtube.com/user/' in url) or ('www.youtube.com/channel/' in url):
        u = 'plugin://plugin.video.youtube/%s/%s/' % (url.split( '/' )[-2], url.split( '/' )[-1])
        ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
        return ok	
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok	
	
def parameters_string_to_dict(parameters):
    ''' Convert parameters encoded in a URL to a dict. '''
    paramDict = {}
    if parameters:
        paramPairs = parameters[1:].split("&")
        for paramsPair in paramPairs:
            paramSplits = paramsPair.split('=')
            if (len(paramSplits)) == 2:
                paramDict[paramSplits[0]] = paramSplits[1]
    return paramDict

DecryptData = base64.b64decode	
'''homeurl = 'aHR0cDovL3VwbGF5aGQuY29tL3NvdXJjZWNvZGUvaG9tZS54bWw=' '''
homeurl = 'aHR0cDovL3JlcG9zLmNoYXVraGFuZy10ZWNoLmNvbS9ob21lLnhtbA=='
params=parameters_string_to_dict(sys.argv[2])
mode=params.get('mode')
url=params.get('url')
name=params.get('name')
iconimage=None

try:
  iconimage=urllib.unquote_plus(params["iconimage"])
except:
  pass

if type(url)==type(str()):
    url=urllib.unquote_plus(url)
sysarg=str(sys.argv[1])

if mode == 'tvchannel':TVChannel(url)
elif mode == 'index':Index(url,iconimage)
elif mode == 'indexgroup':IndexGroup(url)	
elif mode == 'index_group':Index_Group(url)	

	
elif mode=='stream':
    dialogWait = xbmcgui.DialogProgress()
    dialogWait.create('Brought to you by Live-TV', 'Loading video. Please wait...')
    resolveUrl(url)
    dialogWait.close()
    del dialogWait	
elif mode=='play':
    dialogWait = xbmcgui.DialogProgress()
    dialogWait.create('Brought to you by Live-TV', 'Loading video. Please wait...')
    PlayVideo(url,name)
    dialogWait.close()
    del dialogWait
else:Channel()
xbmcplugin.endOfDirectory(int(sysarg))