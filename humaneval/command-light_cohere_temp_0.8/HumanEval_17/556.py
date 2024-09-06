Here is a self-contained Python script that implements the `parse_music` function from the previous prompt:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    music = music_string.split(' ')
    particular note last whole note, or is an "of"-like character. Then, we use the corresponding values from the notes dictionary and return the beats as a list.

# Test cases
parse_music('o o| .| o| o| .| .| .| .| .| o o')
should == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

parse_music('o o o o o| o| o| .| o| o| .| .| .')
should == [4, 4, 4, 4, 1, 2, 1, 1, 1, 2]

parse_music('".o')
should == []

parse_music('x')
should == []
```
This code defines a function called `parse_music` that takes a string as input and returns a list of integers. It does this by checking the string's character and looking up the character in a dictionary to determine the number of beats for that note.