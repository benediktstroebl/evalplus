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

    :param music_string: A string representing musical notes
    :return: A list of integers corresponding to the duration of each note in beats
    """

    # Define a dictionary mapping note representations to their respective durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the note durations
    durations = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the input string
    for char in music_string:
        # If the character is a space, it means we've reached the end of a note
        if char =='':
            # If the current note is not empty, add its duration to the list
            if current_note:
                durations.append(note_durations.get(current_note, 0))
                # Reset the current note
                current_note = ''
        else:
            # Add the character to the current note
            current_note += char

    # Add the duration of the last note if it's not empty
    if current_note:
        durations.append(note_durations.get(current_note, 0))

    return durations


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```