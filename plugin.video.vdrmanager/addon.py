from xbmcswift2 import Plugin
import os

plugin = Plugin()


@plugin.route('/')
def index():
    item = {
        'label': 'Start VDR',
        'path': plugin.url_for('startvdr'),
        'is_playable': False
    }
    return [item]

@plugin.route('/startvdr/')
def startvdr():
    plugin.notify(msg='Starting VDR ..', title='', delay=1000, image='')
    os.system("/storage/.xbmc/addons/service.multimedia.vdr-addon/bin/switch.sh")
    
if __name__ == '__main__':
    plugin.run()
