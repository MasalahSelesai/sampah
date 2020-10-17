 
import os,sys,time
from time import sleep

def load(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./12)
os.system('clear')
sleep(1)
print ("""
\033[1;97m\tTOMBOL TERMUX
\033[1;97mCreator:\033[1;92mNico ID
\033[1;97mGithub :\033[1;92mhttps://github.com/SUHAT-NICO
\033[90m------------------------------
""")
print('\n\033[90m[\033[1;91m!\033[90m] \033[1;96mMengambil File Default Termux\033[1;97m')
sleep(1)
load("\033[90m[\033[1;92m•\033[90m]\033[1;96mLoading\033[90m............\033[1;97m")
sleep (2)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print('\033[90m[\033[1;92m+\033[90m]\033[1;92mSuccess\033[1;97m')
sleep(2)
print('\n\033[90m[\033[1;91m!\033[90m] \033[1;96mMenambahkan Tombol Termux\033[1;97m')
sleep(1)
load("\033[90m[\033[1;92m•\033[90m]\033[1;96mLoading\033[90m............\033[1;97m")

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
xmanz = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
xmanz.write(key)
xmanz.close()
sleep (2)
os.system('termux-reload-settings')
print ("\033[90m[\033[1;92m+\033[90m]\033[1;92m Success\033[1;97m")
sleep (2)
sys.exit()
