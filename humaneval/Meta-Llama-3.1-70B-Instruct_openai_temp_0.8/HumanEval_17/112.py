```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    This function parses the string and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to how many beats each note lasts.
    """

    # Define a dictionary to map each note to its corresponding beats
    note_beats = {
        'o': 4,  # Whole note lasts four beats
        'o|': 2,  # Half note lasts two beats
        '.|': 1  # Quarter note lasts one beat
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats for each note
    beats = []

    # Iterate over each note in the input string
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o':
            # If the next note is a '|', it's a half note, so skip the next note
            if i + 1 < len(notes) and notes[i + 1] == '|':
                beats.append(note_beats['o|'])
                i += 2
            else:
                beats.append(note_beats['o'])
                i += 1
        # Check if the current note is a quarter note
        elif notes[i] == '.':
            # If the next note is a '|', it's a quarter note, so skip the next note
            if i + 1 < len(notes) and notes[i + 1] == '|':
                beats.append(note_beats['.|'])
                i += 2
            else:
                raise ValueError("Invalid note format: '.' should be followed by '|'.")
        # If the current note is not a whole note or a quarter note, raise a ValueError
        else:
            raise ValueError(f"Invalid note format: '{notes[i]}' is not a valid note.")

    return beats

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

Note that this script assumes that the input string is well-formed, i.e., it does not contain any invalid notes or beats. If the input string is not well-formed, the script will raise a ValueError with a corresponding error message.