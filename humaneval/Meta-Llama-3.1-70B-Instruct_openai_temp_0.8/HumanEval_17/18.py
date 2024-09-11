```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers representing the duration of each note.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string of musical notes in the special ASCII format.

    Returns:
        List[int]: A list of integers representing the duration of each note.
    """
    # Create a dictionary to map notes to their durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the durations
    durations = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the music string
    for char in music_string:
        # If the character is a space, it means we've reached the end of a note
        if char =='':
            # If the current note is not empty, look up its duration and add it to the list
            if current_note in note_durations:
                durations.append(note_durations[current_note])
            # Reset the current note
            current_note = ''
        else:
            # Add the character to the current note
            current_note += char

    # Look up the duration of the last note and add it to the list
    if current_note in note_durations:
        durations.append(note_durations[current_note])

    return durations


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```