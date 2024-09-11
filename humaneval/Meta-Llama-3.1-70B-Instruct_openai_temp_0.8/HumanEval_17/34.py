```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers
    corresponding to how many beats each note lasts.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    :param music_string: A string representing musical notes.
    :return: A list of integers corresponding to the duration of each note in beats.
    """
    # Define a dictionary to map note symbols to their respective durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the note durations
    durations = []

    # Initialize an empty string to build the current note symbol
    current_note = ''

    # Iterate over each character in the input string
    for char in music_string:
        # If the character is not a space, add it to the current note symbol
        if char!='':
            current_note += char
        # If the character is a space, the current note symbol is complete
        else:
            # If the current note symbol is in the note durations dictionary, add its duration to the list
            if current_note in note_durations:
                durations.append(note_durations[current_note])
            # Reset the current note symbol
            current_note = ''

    # Handle the last note symbol, which is not followed by a space
    if current_note in note_durations:
        durations.append(note_durations[current_note])

    return durations


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```