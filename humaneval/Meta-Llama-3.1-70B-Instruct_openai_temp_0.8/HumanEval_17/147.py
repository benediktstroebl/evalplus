```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    and returns a list of integers corresponding to how many beats each note lasts.

    The legend for notes is as follows:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    :param music_string: A string representing musical notes
    :return: A list of integers representing the duration of each note in beats
    """

    # Create a dictionary to map notes to their corresponding durations
    note_durations = {
        'o': 4,  # whole note lasts four beats
        'o|': 2,  # half note lasts two beats
        '.|': 1  # quarter note lasts one beat
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the durations of the notes
    durations = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the input string
    for char in music_string:
        # If the character is a space, it marks the end of a note
        if char =='':
            # Add the duration of the current note to the list
            durations.append(note_durations[current_note])
            # Reset the current note
            current_note = ''
        else:
            # Add the character to the current note
            current_note += char

    # Add the duration of the last note to the list
    durations.append(note_durations[current_note])

    # Return the list of durations
    return durations


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```