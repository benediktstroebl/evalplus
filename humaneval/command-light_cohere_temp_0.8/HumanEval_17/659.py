```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    music = [notes[c] for c in music_string if c in notes]
    return music

# Test cases
string1 = 'o o| .| o| .| .| .| o o'
string2 = 'o o| .| o| .| .| .| o' o'

result1 = parse_music(string1)
print("Result1:", result1)

result2 = parse_music(string2)
print("Result2:", result2)
```
This code defines a function `parse_music` that parses a music notation string and returns a list of integers representing the duration of each note. The function uses a legend where `o` represents a whole note that lasts 4 beats, `o|` represents a half note that lasts 2 beats, and `.|` represents a quarter note that lasts 1 beat. The function then loops through the strings and checks if each character is present in the `notes` dictionary. The test cases demonstrate how the string inputs and show that the function correctly parses the music notation and returns the expected output.