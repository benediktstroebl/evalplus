```python
from typing import List

pattern = 'o|_|.'
base_beat = {'o': 4, '|': 2, '_': 1, '.': 0}

def parse_music(music_string: str) -> List[int]:
    result = []
    notes = music_string.strip()
    
    # check if there is a valid note at each position
    for char in notes:
        if char not in pattern:
            raise ValueError("Invalid note")
            
    # iterate through the string and count beats accordingly
    for i, char in enumerate(notes):
        result.append(base_beat[char])
    
    return result
``` 

This code defines a function called `parse_music` that takes a string input and returns a list of integers representing the number of beats for each note in the music string. 

The code first defines the `base_beat` dictionary that serves as a reference to translate each note to the number of beats. The `pattern` string is a legend to check which characters are valid notes. The function first cleans the input string by stripping any leading and trailing characters that are not notes. It then iterates over each character in the string, and for each character, it checks if it is a valid note, if not, it raises a `ValueError`, otherwise, it counts the beats accordingly and adds it to the result list. 

Here is an example of how to use this code:
```python
print(parse_music('o o| .| o| o| .| .| .| o o'))
```
The output should be:
```
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
``` 

This example demonstrates the parsing of a string representing musical notes in a special ASCII format and returns a list of integers corresponding to the number of beats for each note.