```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers,
    where each integer corresponds to the number of beats each note lasts.

    The legend for notes is:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    :param music_string: A string of musical notes
    :return: A list of integers representing the number of beats each note lasts
    """

    # Create a dictionary to map note representations to their corresponding beat values
    note_beats = {'o': 4, 'o|': 2, '.|': 1}

    # Split the input string into individual notes, using spaces as the delimiter
    notes = music_string.split()

    # Initialize an empty list to store the beat values of the notes
    beats = []

    # Iterate over each note in the list of notes
    for note in notes:
        # If the note has a pipe (|) character, it could be a half or quarter note
        if '|' in note:
            # If the note starts with 'o', it's a half note
            if note.startswith('o'):
                beats.append(note_beats['o|'])
            # Otherwise, it's a quarter note
            else:
                beats.append(note_beats['.|'])
        # If the note doesn't have a pipe character, it's a whole note
        else:
            beats.append(note_beats['o'])

    # Return the list of beat values
    return beats

# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```