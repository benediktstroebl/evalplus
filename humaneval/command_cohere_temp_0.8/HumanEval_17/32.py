```python
from typing import List

PATTERN = {'o': 4, 'o|': 2, '.|': 1}

def parse_music(music_string: str) -> List[int]:
    music_list = []
    beat = 0
    
    for char in music_string:
        if char in 'o|.|':
            beat += PATTERN[char]
        else:
            beat //= 2
        music_list.append(beat)
    
    return music_list
``` 

This code defines a function `parse_music` that takes a string as input and returns a list of integers representing the beats of each musical note. It does this by using a dictionary called `PATTERN` that associates the ASCII characters with the number of beats that they represent. The function iterates over each character in the input string and increments a beat counter based on the beats associated with each ASCII character, except for 'o' which resets the beat counter to 4. The beat count is partitioned by 2 until the next 'o' character is met. Finally, the function returns a list where each element represents the number of beats for each corresponding musical note.