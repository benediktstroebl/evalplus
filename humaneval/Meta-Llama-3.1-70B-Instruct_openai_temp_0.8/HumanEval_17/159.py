```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    parses it, and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes
    :return: A list of integers representing the duration of each note in beats
    """

    # Create a dictionary to map note representations to their corresponding durations
    note_durations = {
        'o': 4,  # whole note lasts four beats
        'o|': 2,  # half note lasts two beats
        '.|': 1  # quarter note lasts one beat
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the durations of the notes
    durations = []

    # Initialize an empty string to build the current note representation
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
            # Add the character to the current note representation
            current_note += char

    # Add the duration of the last note to the list
    if current_note:
        durations.append(note_durations[current_note])

    return durations

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```