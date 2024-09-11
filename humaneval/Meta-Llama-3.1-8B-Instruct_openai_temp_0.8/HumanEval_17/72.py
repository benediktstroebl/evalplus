### Music Note Parser
#### Python Script

```markdown
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    :param music_string: A string representing musical notes.
    :return: A list of integers representing the duration of each note.
    """

    # Define a dictionary to map note types to their durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the note durations
    note_lengths = []

    # Iterate over each note and append its duration to the list
    for note in notes:
        note_lengths.append(note_durations.get(note, 0))  # Return 0 if note is not found

    return note_lengths

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input, parses it, and returns a list of integers representing the duration of each note. The note durations are determined by a dictionary that maps note types to their respective durations. The function splits the input string into individual notes, iterates over them, and appends their durations to a list. Finally, it returns the list of note durations. The script includes a test case to demonstrate the function's usage.