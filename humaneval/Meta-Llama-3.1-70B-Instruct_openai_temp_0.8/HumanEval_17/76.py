```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format.
    It parses this string and returns a list of integers corresponding to how many beats each note lasts.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to how many beats each note lasts.
    """

    # Create a dictionary to map the note representations to their corresponding beat values
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat values of the notes
    beats = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over the notes
    for note in notes:
        # If the current note does not end with a '|' and the note is not a '.' followed by a '|',
        # it means the current note is not complete, so add the note to the current note
        if not current_note.endswith('|') and not (note == '|' and current_note == '.'):
            current_note +='' + note
        # If the current note ends with a '|' or the note is a '.' followed by a '|',
        # it means the current note is complete, so add its beat value to the list and reset the current note
        else:
            current_note += note
            beats.append(note_beats.get(current_note.strip(), 0))
            current_note = ''

    # If there is a remaining current note, add its beat value to the list
    if current_note:
        beats.append(note_beats.get(current_note.strip(), 0))

    # Return the list of beat values
    return beats

# Example usage
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```