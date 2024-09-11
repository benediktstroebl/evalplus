```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function parses a string of musical notes in a special ASCII format and returns a list of integers 
    representing the number of beats each note lasts.

    :param music_string: A string of musical notes
    :return: A list of integers representing the number of beats each note lasts
    """
    # Define a dictionary to map notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats = []

    # Initialize an empty string to build each note
    current_note = ''

    # Iterate over each character in the input string
    for char in music_string:
        # If the character is a space, it means we have a complete note
        if char =='':
            # Add the beats of the current note to the list
            beats.append(note_beats[current_note])
            # Reset the current note
            current_note = ''
        else:
            # Add the character to the current note
            current_note += char

    # Add the beats of the last note to the list
    if current_note:
        beats.append(note_beats[current_note])

    # Return the list of beats
    return beats

# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```