```python
from typing import List

PATTERN = {'o': 4, 'o|': 2, '.': 1}


def parse_music(music_string: str) -> List[int]:
    result = []
    curr_note = 0
    for c in music_string:
        if c in 'o|.":':
            result.append(curr_note)
            curr_note = PATTERN[c]
        else:
            curr_note //= 2
    result.append(curr_note)
    return result
``` 

This code defines a function `parse_music` that takes a string representation of musical notes in the specified format and returns a list of integers representing the number of beats for each note.

The `parse_music` function starts by initializing an empty list called `result` to store the computed beats. Then it sets `curr_note` to 0 to represent the current note value. It iterates through each character in the input string `music_string`, if the character is part of the `PATTERN` it updates `result` by adding the current note value and updates `curr_note` to the value of the current note. If the character is not part of the valid note characters, then the current note is halved, this is because the current note is supposed to be concatenated with another note, and this represents the half value of the previous note. Finally, the function returns the `result` list. 

This solution is relatively efficient, with a time complexity of O(n), where n is the length of the input string `music_string`, because it checks each character in the string only once. 

It is important to note that in the interest of making this code concise and self-contained, this code is not suited for production-level codebase. In a real-world scenario, you would want to consider handling other punctuation characters, adding error-handling mechanisms, and refining the input parsing logic using more sophisticated libraries.