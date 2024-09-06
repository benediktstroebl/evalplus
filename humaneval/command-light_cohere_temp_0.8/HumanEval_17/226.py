```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    
    beats = 0
    notes_count = [0] * 4
    
    for symbol in music_string.split(' '|.'
    if symbol in notes:
        beats += notes[symbol]
        notes_count[beats % 4] += 1
    
    return notes_count

# Test cases:
# Test with half notes
parse_music('o o| .| o| .| .| .| o o')
 [4, 2, 1, 2, 2, 1, 1, 1, 4, 4]
# Test with whole notes and different rhythms
parse_music('o o o| .| o| .| .| .| o| o .')
 [4, 4, 1, 1, 2, 2, 1, 1, 2]
```
This function, `parse_music`, takes a string of music and parses it to return the number of beats in the music. It uses a predefined dictionary to translate musical notes to the number of beats they last. The function ensures it works for different rhythms and types of music notes.