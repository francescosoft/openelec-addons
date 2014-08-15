from xbmcswift2 import Plugin
import os

plugin = Plugin()


@plugin.route('/')
#@cached_route()
def index():
    item = {
        'label': 'Start VDR',
        'path': plugin.url_for('startvdr'),
        'is_playable': False
    }
    return [item]

@plugin.route('/startvdr/')
#@cached_route()
def startvdr():

    #plugin.notify(msg='Starting VDR ..', title='', delay=1000, image='')
    if os.path.isfile("/storage/.config/udev.rules.d/66-libcec-daemon.rules"):
    	plugin.notify(msg='Starting VDR ..', title='', delay=1000, image='')
    	os.system("/storage/.xbmc/addons/service.multimedia.vdr-addon/bin/switch.sh")
    else:
        if os.path.isfile("/storage/.xbmc/addons/service.multimedia.vdr-addon/bin/init.sh"):
    	   #print "Storage path is : %s" % plugin.storage_path
    	   plugin.notify(msg='Init Plugin and restart', title='', delay=1000, image='')
           os.system("/storage/.xbmc/addons/service.multimedia.vdr-addon/bin/init.sh")
        else:
            plugin.notify(msg='Please install the VDR Addon first', title='', delay=5000, image='')
    
if __name__ == '__main__':
    plugin.run()
