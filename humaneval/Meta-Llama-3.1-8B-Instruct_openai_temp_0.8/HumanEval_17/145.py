### Music Note Parser
#### Solution

Here is a Python script that solves the problem:

```markdown
### Music Note Parser
#### Solution

```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    This function parses this string and returns list of integers corresponding to how many beats does each
    note last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers corresponding to how many beats does each note last.
    """
    music_dict = {'o': 4, 'o|': 2, '.|': 1}
    notes = music_string.split()
    beats = [music_dict[note] for note in notes]
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

#### Explanation

This script defines a function `parse_music` that takes a string of musical notes as input. It uses a dictionary `music_dict` to map each note to its corresponding beat count. The function then splits the input string into individual notes, looks up each note in the dictionary, and returns a list of beat counts.

The test case at the end demonstrates how to use the function. You can replace the test case with your own input string to see the function in action.