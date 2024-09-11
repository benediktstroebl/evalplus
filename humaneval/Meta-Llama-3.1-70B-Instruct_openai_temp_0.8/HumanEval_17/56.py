```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers.
    Each integer in the list corresponds to the number of beats a note lasts.

    :param music_string: A string of musical notes.
    :return: A list of integers representing the number of beats each note lasts.
    """

    # Create a dictionary to map each note type to its duration
    note_durations = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }

    # Initialize an empty list to store the note durations
    durations = []

    # Initialize an empty string to build each note
    note = ''

    # Iterate over each character in the music string
    for char in music_string:
        # If the character is a space, it means we've reached the end of a note
        if char =='':
            # If the note is not empty, add its duration to the list
            if note:
                durations.append(note_durations[note.strip()])
                note = ''
        else:
            # Add the character to the note
            note += char

    # Add the duration of the last note
    if note:
        durations.append(note_durations[note.strip()])

    return durations

print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```