```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers 
    corresponding to how many beats each note lasts.

    Args:
    music_string (str): A string representing musical notes.

    Returns:
    List[int]: A list of integers representing the duration of each note in beats.

    """
    # Define a dictionary to map each note to its duration
    note_durations = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the durations of the notes
    durations = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the input string
    for char in music_string:
        # If the character is a space, it means we've reached the end of a note
        if char =='':
            # If the current note is not empty, add its duration to the list
            if current_note:
                durations.append(note_durations[current_note])
                current_note = ''
        else:
            # Add the character to the current note
            current_note += char

    # Add the duration of the last note to the list
    if current_note:
        durations.append(note_durations[current_note])

    return durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```