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

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.
    """

    # Define a dictionary to map note symbols to their corresponding beat counts
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beat counts
    beat_counts = []

    # Initialize an empty string to build the current note symbol
    current_note = ''

    # Iterate over each character in the music string
    for char in music_string:
        # If the character is a space, it means we've reached the end of a note symbol
        if char =='':
            # If the current note symbol is not empty, add its beat count to the list
            if current_note:
                beat_counts.append(note_beats.get(current_note, 0))
                current_note = ''
        else:
            # Add the character to the current note symbol
            current_note += char

    # Add the beat count of the last note symbol to the list
    if current_note:
        beat_counts.append(note_beats.get(current_note, 0))

    return beat_counts


# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```