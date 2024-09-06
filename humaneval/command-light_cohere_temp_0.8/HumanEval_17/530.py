```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse the music_string representing notes in a special ASCII format.
    This legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat
    Return list of integers corresponding to how many beats does each note last.

 music_string: str = input("Enter music string: ")
 notes = []
 beat_rate = 4  # default beats per whole note
for note in music_string. note: format = "o{0}|{1}" if 'o' in note else "o|{0}" if '|' in note else ".|{0}" 
    if ' ' not in note:
        notes.append(int(note) / beat_rate)
    else:
        notes.append(int(note[0]) * beat_rate)
 return notes

# Test
music_string = "o o| .| o| .| .| .| o o"
result = parse_music(music_string)
print(result)
```