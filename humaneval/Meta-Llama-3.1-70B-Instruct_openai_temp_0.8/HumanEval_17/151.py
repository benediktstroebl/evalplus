```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers
    corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes
    :return: A list of integers representing the duration of each note in beats
    """
    # Create a dictionary to map each note to its duration
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the durations of the notes
    durations = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the input string
    for char in notes:
        # If the character is a space, it means we've reached the end of a note
        if char == '':
            # Add the duration of the current note to the list of durations
            durations.append(note_durations[current_note])
            # Reset the current note
            current_note = ''
        else:
            # Add the character to the current note
            current_note = char

            # If the current note is in the dictionary, it means we've reached the end of a note
            if current_note in note_durations:
                # Add the duration of the current note to the list of durations
                durations.append(note_durations[current_note])
                # Reset the current note
                current_note = ''

    # Return the list of durations
    return durations


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```