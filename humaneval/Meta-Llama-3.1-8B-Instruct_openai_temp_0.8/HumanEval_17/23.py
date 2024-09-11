```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format.

    Args:
    music_string (str): A string representing musical notes.
    
    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.

    """
    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat lengths
    beat_lengths = []

    # Iterate over each note in the notes list
    for note in notes:
        # Use if-elif-else statements to determine the beat length based on the note
        if note == 'o':
            # 'o' represents a whole note, which lasts 4 beats
            beat_lengths.append(4)
        elif note == 'o|':
            # 'o|' represents a half note, which lasts 2 beats
            beat_lengths.append(2)
        elif note == '.|':
            # '.|' represents a quarter note, which lasts 1 beat
            beat_lengths.append(1)

    # Return the list of beat lengths
    return beat_lengths

# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string representing musical notes as input, parses the string, and returns a list of integers corresponding to the number of beats each note lasts. The function uses if-elif-else statements to determine the beat length based on the note. The example usage demonstrates how to use the function with the provided test case.