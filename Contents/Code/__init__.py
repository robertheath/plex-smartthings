from smartthings import smartthings
import json

NAME = "SmartThings"
ART             = 'art-default.jpg'
ICON            = 'icon-default.png'

####################################################################################################
def Start():
    Plugin.AddViewGroup("InfoList", viewMode="InfoList", mediaType="items")

    ObjectContainer.title1 = NAME
    ObjectContainer.view_group="InfoList"
    ObjectContainer.art = R(ART)

####################################################################################################
@handler('/applications/smartthings/hubs', NAME)
def MainMenu():
    oc = ObjectContainer()

    api = smartthings(username=Prefs['smUser'], password=Prefs['smPass'])

    hubs = api.hubs()
#    Log(type(hubs))
    for hub in hubs:
#        Log(hub['id'])
#        Log(hub['name'])
	oc.add(DirectoryObject(key = hub['id'], title = hub['name'], thumb = R("hub-on.png")))
#	for s in hub:
#		Log(s)
#		Log(hub[s])

    return oc

####################################################################################################
@route('/applications/smartthings/hubs/{key}')
def ProcessRequest(key):
    oc = ObjectContainer()

    api = smartthings(username=Prefs['smUser'], password=Prefs['smPass'])
    	
#    hub = api.hub(key)
#    Log(hub)

    devices = api.hub_devices(key)
    for device in devices:
	image = ""
#	filename = ""
#	for s in device:
#	    Log(s)
#	    Log(device[s])
#	Log(device['type'])
	stateOverrides = device['stateOverrides']
	for x in stateOverrides:
	    image = x['icon']
	    Log(image)
#	    if (image == "st.switches.switch.on" or image == "st.switches.switch.off"):
#	        filename = image
#	    else:
#	        filename = image+"-icn"

#	    Log(filename)
#	    for y in x:
#	        Log(y)
#               Log(x[y])

        currentStates = device['currentStates']
        for t in currentStates:
		if (t['name'] == "temperature" or t['name'] == "battery" or t['name'] == "humidity" or t['name'] == "water"):
		    icon = Resource.ContentsOfURLWithFallback("http://dummyimage.com/512X512/fff/000.png&text="+t['value'])
		    label = t['name'].title()
		else:
		    icon = R(image+"-"+t['value']+".png")
		    label = device['label']
		oc.add(DirectoryObject(key = device['id'], title = label, summary = t['name']+" is "+t['value'], thumb = icon))
#	    for u in t:
#                Log(u)
#                Log(t[u])

    return oc
