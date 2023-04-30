# Hyle Ver 1.4.8.8
# made by Elkyw with ❤
import os
import wave
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f', help='Select Audio File', dest='audiofile')
parser.add_argument('-m', help='Enter your Secret Message', dest='secretmsg')
parser.add_argument('-o', help='Your Output file path and name', dest='outputfile')
args = parser.parse_args()
af = args.audiofile
string = args.secretmsg
output = args.outputfile
arged = False
if af and string and output:
    arged = True
def cls():
  os.system("clear")
def help():
  print("\033[92mHide Your Secret Message in Audio Wave File.\033[0m")
  print ('''usage:python3 Hyle.py [-h] [-f AUDIOFILE] [-m SECRETMSG] [-o OUTPUTFILE]

optional arguments:
  -h, --help    show this help message and exit
  -f AUDIOFILE  Select Audio File
  -m SECRETMSG  Enter your message
  -o OUTPUTFILE Your output file path and name''')
  
def banner():
    print ('''                                                                    
\033[1;31m 
                                                                            
                                                                            
HHHHHHHHH     HHHHHHHHH                         lllllll                     
H:::::::H     H:::::::H                         l:::::l                     
H:::::::H     H:::::::H                         l:::::l                     
HH::::::H     H::::::HH                         l:::::l                     
  H:::::H     H:::::H  yyyyyyy           yyyyyyy l::::l     eeeeeeeeeeee    
  H:::::H     H:::::H   y:::::y         y:::::y  l::::l   ee::::::::::::ee  
  H::::::HHHHH::::::H    y:::::y       y:::::y   l::::l  e::::::eeeee:::::ee
  H:::::::::::::::::H     y:::::y     y:::::y    l::::l e::::::e     e:::::e
  H:::::::::::::::::H      y:::::y   y:::::y     l::::l e:::::::eeeee::::::e
  H::::::HHHHH::::::H       y:::::y y:::::y      l::::l e:::::::::::::::::e 
  H:::::H     H:::::H        y:::::y:::::y       l::::l e::::::eeeeeeeeeee  
  H:::::H     H:::::H         y:::::::::y        l::::l e:::::::e           
HH::::::H     H::::::HH        y:::::::y        l::::::le::::::::e          
H:::::::H     H:::::::H         y:::::y         l::::::l e::::::::eeeeeeee  
H:::::::H     H:::::::H        y:::::y          l::::::l  ee:::::::::::::e  
HHHHHHHHH     HHHHHHHHH       y:::::y           llllllll    eeeeeeeeeeeeee  
                             y:::::y                                        
                            y:::::y                                         
                           y:::::y                                          
                          y:::::y                                           
                         yyyyyyy     \033[0m \033[1;35mBy-\033[0m \033[1;36mElkyw@programmer.net\033[0m''')

def em_audio(af, string, output):
    if not arged:
      help()
    else:
      print ("Please wait...")
      waveaudio = wave.open(af, mode='rb')
      frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
      string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
      bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
      for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
      frame_modified = bytes(frame_bytes)
      with wave.open(output, 'wb') as fd:
        fd.setparams(waveaudio.getparams())
        fd.writeframes(frame_modified)
      waveaudio.close()
      print ("Done...")
cls()
banner()
try:
  em_audio(af, string, output)
except:
  print ("Something went wrong!! try again")
  quit('')
