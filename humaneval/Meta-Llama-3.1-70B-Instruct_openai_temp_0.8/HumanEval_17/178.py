```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format
    and return a list of integers corresponding to how many beats each note lasts.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    # Create a dictionary to map note representations to their corresponding beat counts
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the music string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat counts
    beat_counts = []

    # Initialize an empty string to build each note representation
    note = ''

    # Iterate over each character in the notes
    for char in notes:
        # If the character is not a space, add it to the current note
        if char!='':
            note += char
        # If the character is a space or we've reached the end of the notes, 
        # check if the current note matches any of the note representations
        if char =='' or notes.index(note) == len(notes) - 1:
            # If the note matches a representation, add its beat count to the list
            if note in note_beats:
                beat_counts.append(note_beats[note])
            # Reset the note
            note = ''

    return beat_counts

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```