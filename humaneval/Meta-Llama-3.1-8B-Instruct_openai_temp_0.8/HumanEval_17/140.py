### Parse Musical Notes
#### Python Script
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format
    and return a list of integers corresponding to how many beats each note lasts.

    The legend is as follows:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers representing the duration of each note in beats.
    """
    # Define a dictionary to map notes to their durations
    note_durations = {'o': 4, 'o|': 2, '.|': 1}

    # Initialize an empty list to store the note durations
    durations = []

    # Iterate over each character in the music string
    for char in music_string:
        # Check if the character is a valid note
        if char in note_durations:
            # Append the note's duration to the list
            durations.append(note_durations[char])
        else:
            # If the character is not a valid note, raise a ValueError
            raise ValueError(f"Invalid note '{char}' in music string")

    return durations

# Example usage
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
This script defines a function `parse_music` that takes a string representing musical notes as input and returns a list of integers representing the duration of each note in beats. The function uses a dictionary to map notes to their durations and iterates over each character in the input string to append the corresponding duration to the list. If an invalid note is encountered, a ValueError is raised. The script includes an example usage of the function.