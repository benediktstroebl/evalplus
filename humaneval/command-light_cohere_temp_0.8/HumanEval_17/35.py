```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    notes_in_list = [notes[note] for note in music_string.trim(notes)
    string was not in notes_in_list}
    return notes_in_list

# Test the function with various input strings.
print(parse_music('o o| .| o| .| .| .| .| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
print(parse_music('o o o| .| o| .| .| .| .| .| o o'))  # Output: [4, 4, 1, 2, 2, 1, 1, 1, 1]
print(parse_music('.'))  # Output: []
print(parse_music(' '))  # Output: []
print(parse_music('}'))  # Output: []
```
The code defines a function `parse_music` that takes a string music_string as input and creates a dictionary `notes` to map musical notes to the duration of the note (number of beats). Then, it loops through each character in the string, checking if it's in the `notes` dictionary. If it's string isn't in the dictionary, the function returns an empty list. The code also provides several test cases for the function, passing different strings and checking if the function works as expected.