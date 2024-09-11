```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers 
    corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers corresponding to the number of beats each note lasts.

    Example:
        >>> parse_music('o o|.| o| o|.|.|.|.| o o')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """

    # Define a dictionary to map each note to its corresponding beats
    note_to_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the input string
    for char in music_string:
        # If the character is a space, add the current note to the list and reset it
        if char =='':
            # If the current note is not empty, add it to the list
            if current_note:
                # Map the current note to its corresponding beats and add it to the list
                beats.append(note_to_beats.get(current_note, 0))
                current_note = ''
        else:
            # Add the character to the current note
            current_note += char

    # Add the last note to the list
    if current_note:
        beats.append(note_to_beats.get(current_note, 0))

    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```