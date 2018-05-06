#!/usr/local/bin/python3
import os
import subprocess
import re
from datetime import datetime

# Determine city
location_raw = os.popen('/usr/local/bin/whereami').read()
long_line = location_raw.splitlines()[0]
lat_line = location_raw.splitlines()[1]
longlat = long_line.split(':')[1].strip() + ',' + lat_line.split(':')[1].strip()

# Determine sunrise/sunset
sun_raw = os.popen('/usr/local/bin/solunar -l %s' % longlat).read()
sunrise = re.search('Sunrise: (\d*:\d*)', sun_raw).group(1)
sunset = re.search('Sunset: (\d*:\d*)', sun_raw).group(1)
sunrise = datetime.strptime(sunrise, '%H:%M').time()
sunset = datetime.strptime(sunset, '%H:%M').time()
present = datetime.now().time()

set_wallpaper_script = """/usr/bin/osascript<<END
tell application "System Events"
    tell every desktop
        set picture to "%s"
    end tell
end tell
END"""

# Return 0 if sun is down
if present < sunrise or present > sunset:
    # Night
    subprocess.Popen(set_wallpaper_script%'/Users/welcomattic/Pictures/wallpapers/sunset.jpg', shell=True)
    os.popen('/usr/local/bin/dark-mode on')
    exit(0)
else:
    # Day
    subprocess.Popen(set_wallpaper_script%'/Users/welcomattic/Pictures/wallpapers/sunrise.jpg', shell=True)
    os.popen('/usr/local/bin/dark-mode off')    
    exit(1)
