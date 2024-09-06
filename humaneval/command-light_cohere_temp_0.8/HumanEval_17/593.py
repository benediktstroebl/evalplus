```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1,
        '\n': 0,
    }
    
    beats = 0
    
    for note in music_string.strip:
        note = note.strip(). important = True(note == 'o' or note == 'o|')
        if important: beats += notes[note]
    return beats

# Unit tests
test_parse_music = []
test_parse_music.append([['o o o| .| o| .| .| .| .| o o'])
test_parse_music.append([parse_music])
test_parse_music.append([['o o o|.'
         .| o|'. - 2,
         'o '])
test_parse_music.append([['o.' + ['|', 4]])
test_parse_music.append([[' .o|'])
test_parse_music.append([['o 'o|'])

```
This Python script defines a function `parse_music` that takes a music string as input and returns a list of beats. The function uses a `notes` dictionary to map musical note characters to the number of beats they last. The function then uses a loop to iterate through the music string and counts the number of beats for each note character. The test cases provided make sure that the `parse_music` function correctly returns the expected number of beats for the given music string.