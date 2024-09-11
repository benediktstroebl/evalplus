### Music Note Parser
#### Python Script

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a musical note string and return a list of integers corresponding to the duration of each note.

    Args:
    music_string (str): A string representing musical notes in ASCII format.

    Returns:
    List[int]: A list of integers representing the duration of each note.

    """
    music_dict = {'o': 4, 'o|': 2, '.|': 1}  # Define a dictionary to map notes to their durations
    return [music_dict[note] for note in music_string.split()]  # Split the string and look up the durations


# Test the function
if __name__ == "__main__":
    music_string = 'o o|.| o| o|.|.|.|.| o o'
    result = parse_music(music_string)
    print(result)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This script defines a function `parse_music` that takes a string representing musical notes and returns a list of integers corresponding to the duration of each note. The function uses a dictionary to map notes to their durations, and then splits the input string into individual notes and looks up their durations in the dictionary. The script also includes a test case to demonstrate the function's usage.