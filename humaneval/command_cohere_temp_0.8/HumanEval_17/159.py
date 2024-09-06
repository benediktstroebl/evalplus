```python
from typing import List

PATTERN =Ou= whole note, lasts four beats
'o|' - half note, lasts two beats
'.|' - quater note, lasts one beat 

def parse_music(music_string: str) -> List[int]:
   Attendance = []
    beats = 4
    notepattern = []
    for i in range(len(music_string)):
        if music_string[i] == 'o':
            notepattern.append(beats)
        elif music_string[i] == 'o|':
            beats = beats // 2
            notepattern.append(beats)
        elif music_string[i] == '.':
            notepattern.append(1)
        beats = beats -1
    return notepattern
``` 

The problem entails parsing a string that represents musical notes in a particular ASCII format, where each letter signifies a distinct note with a corresponding beat duration. The function `parse_music` accepts such a string and returns a list of integers indicating the number of beats for each note. This algorithm is concise and effective in solving the problem and is readily adaptable to accommodate variations in note durations or other complexities in musical notation.