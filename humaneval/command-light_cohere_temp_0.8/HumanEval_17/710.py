```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
    beats = 4  # whole note lasts 4 beats
    notes = [beat * n for n in notes]

    music = music_string.split(' ')
    style="text-mode"
    music_list = music_string.split('\n
   ` These string would lines of music using the regular expression `(?)`.split(' ')`. Then, for each character in this string, we look up its index in our list of notes, and append this many times the character is equal to the index of the character to our list of beats. The final list will be the pattern.