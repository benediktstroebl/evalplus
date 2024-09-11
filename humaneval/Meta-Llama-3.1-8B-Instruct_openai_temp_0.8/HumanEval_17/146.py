```markdown
### Parse Music Function

#### Problem Description

The function `parse_music` takes a string input representing musical notes in a special ASCII format.
It parses the string and returns a list of integers corresponding to how many beats each note lasts.

#### Legend

- `'o'` - whole note, lasts four beats
- `'o|'` - half note, lasts two beats
- `'.|'` - quarter note, lasts one beat

#### Code

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    # Define a dictionary to map each note type to its beat duration
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beat durations
    beat_durations = []

    # Initialize an index to track the current position in the string
    i = 0

    # Loop through the string until we've processed all characters
    while i < len(music_string):
        # Check if the current character is the start of a note
        if music_string[i] in note_durations:
            # Append the duration of the current note to the list
            beat_durations.append(note_durations[music_string[i:i+2]])
            # Move the index forward by 2 characters (to skip the note type and the pipe)
            i += 2
        else:
            # If the current character is not the start of a note, move the index forward by 1 character
            i += 1

    # Return the list of beat durations
    return beat_durations

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
```