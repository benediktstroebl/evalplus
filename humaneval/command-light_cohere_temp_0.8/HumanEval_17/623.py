```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    beats = music_string.split(' ')
    of note -> beats.split('|') 
    notes = dict(zip(beats, notes))
    return [beat // 4 for beat in notes.

if __name__ == "__main__":
    music_string = input("Enter the music string: ")
    print(parse_music(music_string)) )
``` 
The function parse_music takes a string of music notes and returns a list of integers corresponding to the number of beats of each note. The notes dictionary maps the known musical note characters to their respective beat values.