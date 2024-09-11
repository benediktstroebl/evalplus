### Musical Note Parser
#### A Python Script to Parse Musical Notes and Calculate Their Respective Beat Durations

```markdown
### Code

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format
    and returns a list of integers corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string of musical notes in the format 'o', 'o|', '.|'

    Returns:
        List[int]: A list of integers representing the beat duration of each note
    """
    # Define a dictionary to map note-to-beat duration
    note_to_beat = {'o': 4, 'o|': 2, '.|': 1}

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store beat durations
    beat_durations = []

    # Iterate over each note in the input string
    for note in notes:
        # Append the corresponding beat duration to the list
        beat_durations.append(note_to_beat[note])

    # Return the list of beat durations
    return beat_durations

# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

### Explanation

This script defines a function `parse_music` that takes a string `music_string` as input. It first splits the input string into individual notes using the `split` method. Then, it defines a dictionary `note_to_beat` to map each note to its corresponding beat duration. Finally, it iterates over each note in the input string, appends the corresponding beat duration to a list `beat_durations`, and returns this list.

### Example Use Case

The example usage demonstrates how to call the `parse_music` function with a sample input string and prints the resulting list of beat durations.

### Commit Message

`Added musical note parser to calculate beat durations`

### API Documentation

```markdown
### parse_music(music_string: str) -> List[int]

This function takes a string representing musical notes in a special ASCII format
and returns a list of integers corresponding to how many beats each note lasts.

Args:
    music_string (str): A string of musical notes in the format 'o', 'o|', '.|'

Returns:
    List[int]: A list of integers representing the beat duration of each note
```