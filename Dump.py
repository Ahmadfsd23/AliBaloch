import os, platform, time

try:

    import rich

    os.system('pip install rich')

    import requests

except:

    os.system('pip install requests')

os.system('git pull')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    print("\n\x1b[1;92m Congratulations ! Your Device Support Tolls\033[1;37m")

    os.system('xdg-open https://facebook.com/groups/1017905562448002/');time.sleep(5)

    from Dp import Menu

    Menu()

elif bit == '32bit':

    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")
