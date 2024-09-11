```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format, 
    and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers representing the duration of each note.
    """
    # Define a dictionary to map notes to their corresponding durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the durations of the notes
    durations = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the notes
    for char in notes:
        # If the character is 'o' or '.', it's the start of a new note
        if char in ['o', '.']:
            # If we've already built a note, add its duration to the list
            if current_note:
                durations.append(note_durations[current_note])
            # Reset the current note to the new character
            current_note = char
        # If the character is '|', it's the end of the current note
        elif char == '|':
            # Add the current note and '|' to the note_durations dictionary key
            current_note += '|'
            # Add the duration of the current note to the list
            durations.append(note_durations[current_note])
            # Reset the current note
            current_note = ''

    # If the last note didn't end with '|', add its duration to the list
    if current_note:
        durations.append(note_durations[current_note])

    return durations


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```