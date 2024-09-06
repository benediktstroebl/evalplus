Here is a Python script that contains a self-contained function that solves the problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    
    beats = [notes[c] for c in music_string if c in notes]
    
    return beats

# Test the function with different inputs
test_parse_music = parse_music('o o| .| o| .| .| .| .| o o')
print(test_parse_music)
``` 
This function takes a string of music notes represented in a special ASCII format. 

The function then creates a dictionary where keys are musical notes and values are the beat count. 

The function then iterates through each character in the string and checks if it's a valid musical note. 

Finally, it returns a list of beats that matches the provided music.