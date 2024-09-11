```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format
    and return a list of integers corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string of musical notes in ASCII format.

    Returns:
        List[int]: A list of integers representing the number of beats for each note.

    Example:
        >>> parse_music('o o|.| o| o|.|.|.|.| o o')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """

    # Create a dictionary to map note symbols to their corresponding beat counts
    note_beat_map = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beat counts
    beat_counts = []

    # Initialize an empty string to build the current note symbol
    current_note = ''

    # Iterate over each character in the input string
    for char in music_string:
        # If the character is a space, it marks the end of a note symbol
        if char =='':
            # If the current note symbol is not empty, add its beat count to the list
            if current_note:
                beat_counts.append(note_beat_map.get(current_note, 0))
                # Reset the current note symbol
                current_note = ''
        else:
            # Add the character to the current note symbol
            current_note += char

    # Handle the last note symbol
    if current_note:
        beat_counts.append(note_beat_map.get(current_note, 0))

    return beat_counts

# Example usage:
music_string = 'o o|.| o| o|.|.|.|.| o o'
beat_counts = parse_music(music_string)
print(beat_counts)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```