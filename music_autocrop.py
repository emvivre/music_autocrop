#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- mode: Python -*-

"""
  ===========================================================================

  Copyright (C) 2017 Emvivre

  This file is part of MUSIC_CROP.

  MUSIC_CROP is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  MUSIC_CROP is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with MUSIC_CROP.  If not, see <http://www.gnu.org/licenses/>.

  ===========================================================================
*/
"""

import soundfile
import sys
import io
import subprocess

def time2str( t, sample_rate ):
    t_sec = t * 1. / sample_rate
    (h, m) = (int(t_sec/(60*60)), int(t_sec/60) % 60)
    s = t_sec - (h * 60 * 60 + m * 60)
    return '%02d:%02d:%02.2f' % (h, m, s)

if len(sys.argv) < 3:
    print 'Usage: %s <INPUT_MUSIC_FILE> <OUTPUT_MUSIC_FILE>' % sys.argv[0]
    quit(1)

(input_file, output_file) = sys.argv[1:]
sp = subprocess.Popen('avconv -i "%s" -f wav -' % input_file, shell=True, stdout=subprocess.PIPE)
(stdout, stderr) = sp.communicate()

s = soundfile.SoundFile( io.BytesIO( stdout ) )
sample_rate = s.samplerate
nb_sample = len( s )
d = s.read( nb_sample )

beg_found = False
for beg_i in range(nb_sample):
    if max(d[ beg_i ]) > 0:
        beg_found = True
        break

if beg_found == False:
    print 'ERROR: all music is empty !'
    quit(1)

end_found = False
for end_i in range(nb_sample-1, beg_i, -1):
    if max(d[ end_i ]) > 0:
        end_found = True
        break

if end_found == False:
    print 'ERROR: unable to found ending !'
    quit(1)

ss_str = time2str( beg_i, sample_rate )
t_str = time2str( end_i - beg_i, sample_rate )
src_fmt = input_file.split('.')[-1]

sp = subprocess.Popen('avconv -y -i %s -ss %s -t %s -f %s -c copy -' % (input_file, ss_str, t_str, src_fmt), shell=True, stdout=subprocess.PIPE)
(stdout, stderr) = sp.communicate()
open(output_file, 'w+').write( stdout )




