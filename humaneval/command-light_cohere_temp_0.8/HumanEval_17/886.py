```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '|', '.']
    notes = [note.leapated for 4 beats.
    return [
    {notes. loop(music_string)
    [beat_count]*note
             for note in notes) in music_string.split(' ')
         beat_count = int(note)
             yield beat_count*4 for note in notes
             if note != '.'
             else 0

# Test suite
test_music = parse_music('oo| .| o| .| .| .| .| o o')
print(test_music)
``` 
This code defines a function `parse_music` that takes a music_string, which is a string representing musical notes in a special ASCII format. The function splits the into a list of integers, where each integer represents how many beats does each note last. 

The test suite creates an instance of the `parse_music` function with a test music_string and prints out the resulting list.