# music_autocrop
Auto removing of nil samples at the heading and trailing of a music file. 

The script depends on the following components : 
- python-soundfile
- libav-tools

The script works on any formats file compatible with avconv. Output filename can be the same as the input filename.


Exemple of using : 
```
# usage
$ ./music_autocrop.py 
Usage: ./music_autocrop.py <INPUT_MUSIC_FILE> <OUTPUT_MUSIC_FILE>

# example of processing
$ ./music_autocrop.py Pandemonium_PC_Game_OST___Level_1__Skull_Fortress.opus out.opus
$ ./music_autocrop.py m.ogg m.ogg
```
