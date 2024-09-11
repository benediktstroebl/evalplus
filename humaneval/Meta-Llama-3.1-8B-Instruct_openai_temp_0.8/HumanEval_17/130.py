```markdown
### Music Note Parser
#### A Python Function to Parse Musical Notes and Return Beat Durations

```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers corresponding to the duration of each note.

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers representing the duration of each note in beats.

    Legend:
    - 'o' - whole note, lasts 4 beats
    - 'o|' - half note, lasts 2 beats
    - '.|' - quarter note, lasts 1 beat
    """

    # Dictionary to map note types to their durations
    note_duration = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beat durations
    beat_durations = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note in the list
    for note in notes:
        # Check if the note is in the dictionary
        if note in note_duration:
            # If it is, append its duration to the list
            beat_durations.append(note_duration[note])
        else:
            # If not, raise a ValueError with a descriptive message
            raise ValueError(f"Unknown note type: '{note}'")

    # Return the list of beat durations
    return beat_durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This Python script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the duration of each note in beats. The function uses a dictionary to map note types to their durations and splits the input string into individual notes before iterating over them to calculate the beat durations. The script also includes a test case to demonstrate the function's usage.