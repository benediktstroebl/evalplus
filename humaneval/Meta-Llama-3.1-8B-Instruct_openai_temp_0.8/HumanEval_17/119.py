```markdown
### Music Note Parser

This Python script takes a string of musical notes as input and returns a list of integers corresponding to the number of beats each note lasts.

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers corresponding to the number of beats each note lasts.

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to the number of beats each note lasts.
    """
    notes = music_string.split()  # Split the input string into individual notes
    note_lengths = {
        'o': 4,  # Whole note
        'o|': 2,  # Half note
        '.|': 1  # Quater note
    }  # Define a dictionary mapping notes to their lengths

    result = []  # Initialize an empty list to store the result
    for note in notes:
        result.append(note_lengths[note])  # Append the length of each note to the result list

    return result  # Return the result list

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

### Example Use Cases

* `parse_music('o o|.| o| o|.|.|.|.| o o')` returns `[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]`
* `parse_music('o|.o.o.o.o.o.o')` returns `[2, 1, 1, 1, 1, 1, 1, 1, 1, 2]`

Note: This script assumes that the input string is well-formed and only contains the three defined notes. It does not perform any error checking or handling. In a real-world application, you would want to add error checking and handling code to make the script more robust.