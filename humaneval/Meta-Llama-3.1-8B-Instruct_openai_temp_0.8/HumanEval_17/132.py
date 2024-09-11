```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers representing the number of beats each note lasts.

    The music string uses the following legend:
    - 'o' - whole note, lasts four beats
    - 'o|' - half note, lasts two beats
    - '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string of musical notes

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts
    """
    # Create a dictionary to map note types to their corresponding beat values
    note_map = {'o': 4, 'o|': 2, '.|': 1}

    # Initialize an empty list to store the parsed notes
    parsed_notes = []

    # Loop through the music string, splitting it into individual notes
    for note in music_string.split():
        # Append the beat value of the current note to the parsed_notes list
        parsed_notes.append(note_map[note])

    # Return the list of parsed notes
    return parsed_notes

# Example usage:
print(parse_music('o o|.| o| o|.|..|.|..|.|. o o'))
```