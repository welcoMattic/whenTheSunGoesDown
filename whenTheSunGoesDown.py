#!/usr/local/bin/python3
import os
import subprocess
import re
from datetime import datetime

# Determine city
location_raw = os.popen('/usr/local/bin/whereami').read()
location_line = location_raw.splitlines()[4]
city = ''.join([i for i in location_line.split(',')[1] if not i.isdigit()]).strip()

# Determine sunrise/sunset
sun_raw = os.popen('/usr/local/bin/solunar -c %s' % city).read()
sunrise = re.search('Sunrise: (\d*:\d*)', sun_raw).group(1)
sunset = re.search('Sunset: (\d*:\d*)', sun_raw).group(1)
sunrise = datetime.strptime(sunrise, '%H:%M').time()
sunset = datetime.strptime(sunset, '%H:%M').time()
present = datetime.now().time()

set_wallpaper_script = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
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
