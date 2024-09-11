```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers
    representing the duration of each note in beats.

    The legend for the notes is as follows:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Args:
        music_string (str): A string of musical notes in the special ASCII format.

    Returns:
        List[int]: A list of integers representing the duration of each note in beats.
    """
    # Create a dictionary to map the notes to their corresponding durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the note durations
    durations = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the music string
    for char in music_string:
        # If the character is a space, it means we've reached the end of a note
        if char =='':
            # If the current note is not empty, add its duration to the list
            if current_note:
                durations.append(note_durations[current_note])
                current_note = ''
        else:
            # If the character is not a space, add it to the current note
            current_note += char

    # After iterating over the entire string, add the duration of the last note
    if current_note:
        durations.append(note_durations[current_note])

    return durations


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```