```python
from typing import List

PATTERN = "o|o|.|"

def parse_music(music_string: str) -> List[int]:
    res = []
    cur_beat = 4
    for note in music_string:
        if note == 'o':
            res.append(cur_beat)
        elif note == '|':
            cur_beat //= 2
        elif note == '.':
            res.append(cur_beat // 4)
        cur_beat //= 4
    return res
``` 

This code defines a single function `parse_music` which takes in a string `music_string` as input and returns a list of integers representing the number of beats corresponding to each note. 

The function uses a predefined pattern of beats represented by the string `PATTERN` which maps each ASCII character to its beat length. It iterates through the characters of the input string `music_string`, updates the current beat's length and appends the current beat to the result list accordingly. Lastly, the result list is returned. 

This solution has a time complexity of `O(n)` where `n` is the length of the input string `music_string`, as it iterates through each character exactly once. It has a space complexity of `O(1)`, as it only stores a few variables and does not require any additional data structures like lists or dictionaries to be created or appended to, resulting in an efficient solution.