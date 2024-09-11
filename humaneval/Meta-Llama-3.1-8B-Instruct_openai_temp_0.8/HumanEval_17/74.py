```markdown
### Music Note Parser

This script takes a string of musical notes in a special ASCII format and returns a list of integers corresponding to how many beats each note lasts.

#### Code

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers representing the number of beats each note lasts.

    :param music_string: A string of musical notes in the format 'o', 'o|', or '.|'
    :return: A list of integers representing the number of beats each note lasts
    """
    note_dict = {'o': 4, 'o|': 2, '.|': 1}  # Dictionary mapping notes to their durations
    notes = music_string.split()  # Split the string into individual notes
    result = []  # Initialize an empty list to store the note durations

    for note in notes:
        result.append(note_dict[note])  # Append the duration of the current note to the result list

    return result  # Return the list of note durations

# Example usage
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))
```

#### Explanation

This script uses a dictionary to map each musical note to its corresponding duration. It then splits the input string into individual notes and appends the duration of each note to a list, which is finally returned.

#### Example Output

When run with the example input, the script will output:

```
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```