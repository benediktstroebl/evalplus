```python
from typing import List

 Pattern = str


def parse_music(music_string: Pattern) -> List[int]:
    """Input to this function is a string representing musical notes in a special ASCII format. 
 Your task is to parse this string and return list of integers corresponding to how many beats does each
note last. 

Here is a legend:
'o' - whole note, lasts four beats
'o|' - half note, lasts two beats
'.|' - quater note, lasts one beat

Example:
'dashed bold notation':
```
parse_music('o o| .| o| o| .| .| .| .| o o')
```
Returns:
 `[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]`
"""
   WholeNote = 4
    HalfNote = 2
    QuarterNote = 1

    beat_values = [WholeNote, HalfNote, QuarterNote]
    parsed_list = []

    current_beat = 0
    for char in music_string:
        if char == 'o':
            current_beat += WholeNote
        elif char == 'o|':
            current_beat += HalfNote
        elif char == '.':
            current_beat += QuarterNote
        else:
            raise ValueError(f"Unexpected char {char}")

        parsed_list.append(current_beat)

    return parsed_list
```

The code defines a function `parse_music` that takes a music string as input and returns a list of beats. 

The code first defines three constants that represent musical notes inside a string: `WholeNote`, `HalfNote`, and `QuarterNote`. Then, `beat_values` creates a list that contains values for these constants. `parsed_list` will store the beats for each note. `current_beat` will keep the cumulative beat count, updated each time the function encounters a new note.

The function checks the current note, and based on the note type, it increments the `current_beat` with the corresponding value from the `beat_values` list. The function finishes the loop and returns the `parsed_list` list that contains the cumulative beat count for each note. 

The provided example in the problem statement returns the list `[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]` as the output example.

The approach has a time complexity of O(n), where n is the length of the input string, as it iterates through each character in the input once, and for each iteration, it performs a constant time operation to update the current beat count. 

The space complexity is O(1) since the function only uses a constant amount of memory to store the current beat count and the list to store the beat counts for each note, irrespective of the input size. 
```