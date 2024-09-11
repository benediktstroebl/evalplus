```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in ASCII format and return a list of integers corresponding to the duration of each note.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string representing musical notes in ASCII format.

    Returns:
        List[int]: A list of integers corresponding to the duration of each note.
    """

    # Create a dictionary to map each note to its corresponding duration
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the durations
    durations = []

    # Iterate over each note
    i = 0
    while i < len(notes):
        # Check if the note is a whole note
        if notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '':
            # If it's a whole note, append its duration to the list and move to the next note
            durations.append(note_durations['o'])
            i += 1
        # Check if the note is a half note or a quarter note
        elif notes[i].endswith('|'):
            # If it's a half note or a quarter note, append its duration to the list and move to the next note
            durations.append(note_durations[notes[i]])
        else:
            # If it's a whole note, append its duration to the list and move to the next note
            durations.append(note_durations['o'])
        i += 1

    # Return the list of durations
    return durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

However, this code still needs a slight adjustment as whole notes are represented in the input string as two characters, 'o' 'o' and 'o' followed by a space. Here is the corrected code:

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in ASCII format and return a list of integers corresponding to the duration of each note.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string representing musical notes in ASCII format.

    Returns:
        List[int]: A list of integers corresponding to the duration of each note.
    """

    # Create a dictionary to map each note to its corresponding duration
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the durations
    durations = []

    # Iterate over each note
    i = 0
    while i < len(notes):
        # Check if the note is a whole note
        if notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == 'o':
            # If it's a whole note, append its duration to the list and move to the next two notes
           