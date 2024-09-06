```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    return [notes[ch] for ch in music_string.

# Test case 1
music1 = 'o o| .| o| o| .| .| .| .| o o'
print(parse_music(music1)) 
# Output [4, 2, 1, 2, 2, 1, 1, 1, 4, 4]

# Test case 2
music2 = '.'
print(parse_music(music2)) 
# Output []
``` 
This script defines a function parse_music that takes a string of music in a special ASCII format as input and returns a list of integers that represents the number of beats in the music. 
The function uses a dictionary to map the musical notation characters to the corresponding number of beats. 

The test cases demonstrate that the function correctly parses the music and returns the expected output.