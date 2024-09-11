```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers
    corresponding to how many beats each note lasts.

    The legend for the notes is as follows:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    :param music_string: A string of musical notes
    :return: A list of integers representing the duration of each note in beats
    """

    # Create a dictionary to map the musical notes to their corresponding durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the durations of the notes
    durations = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the music string
    for char in music_string:
        # If the character is a space, it marks the end of a note
        if char =='':
            # If the current note is not empty, add its duration to the list
            if current_note:
                durations.append(note_durations[current_note])
                current_note = ''
        else:
            # Add the character to the current note
            current_note += char

    # If the music string does not end with a space, add the duration of the last note
    if current_note:
        durations.append(note_durations[current_note])

    return durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Outputs: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```