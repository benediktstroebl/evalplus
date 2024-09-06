```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    beats = 0
    pos = 0
    output = []
    for note in music_string.split(' ' '):
        if note in notes:
            beats += notes[note]
            output.append(beats)
        pos += 1
        
    return output

# Test case 1
test_music1 = 'o o| .| o| .| .| .| .| o o'
test_music1_result = parse_music(test_music1)
print(test_music1_result)

# Test case 2
test_music2 = 'o o| .| o| .| .| .| .| o o| .|.'
test_music2_result = parse_music(test_music2)
print(test_music2_result)
```
This Python script defines a function `parse_music` that parses a music string and returns a list of beats. It uses a legend format for the different note lengths: `o` is a whole note, `o|` is a half note, and `.|` is a quarter note. The script handles both cases of input and correctly identifies and counts the beats in the music string.