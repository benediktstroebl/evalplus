```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = music_string.split(' ')
    whole_notes = [notes[k] for k in music_string.split('\nif pattern matches each whole note, the length of whole_notes matches the length of the notes in our list, and therefore we can index them by 0, 1, 2, 3... to correctly find the half/quarter notes in between.
beats = [k for k in beats if note in notes[k]]
beats = [beat * 4 for beat in beats if note in notes[beat]]
return beats

# Test the function
#Test 1
music_string = 'o o| .| o| .| .| .| .| o o'
print(parse_music(music_string)))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]
#Test 2
music_string = 'o o| o| .' o| .| .| .| o o o'
print(parse_music(music_string)))  # Output: [4, 2, 1, 2, 2, 1, 1, 2, 2]
#Test 3
music_string = 'o o o| .o'
print(parse_music(music_string)))  # Output: [4, 8, 2]
```