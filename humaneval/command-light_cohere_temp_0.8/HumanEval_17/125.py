```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    notes_list = [notes.get(note) for note in music_string.print()
   Example:
        return notes_list

# Test cases
test_parse_music = [
    'o o| .| o| .| .| .| .| o o',
    'o o o| o',
    '|.o .| .',
    '|.|. .',
]

# Function call
result = parse_music(' '.join(test_parse_music))

# Print the result
print(result)
``` 
This solution provides a self-contained function that parses and returns a list of integers representing the number of beats in a given music string. 

Please note that the function uses a dictionary to map music notes to the number of beats that each note represents.  This function is then can be used as a building block for more complex music score applications.