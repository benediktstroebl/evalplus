Here's a self-contained Python script to solve the problem:

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function parses a string representing musical notes in a special ASCII format.
    It returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string of musical notes in a special ASCII format.
    :return: A list of integers representing the duration of each note in beats.
    """
    # Define a dictionary to map musical notes to their corresponding durations
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
    for char in music_string:
        # If the character is a space, it means we've reached the end of a note
        if char =='':
            # Add the duration of the current note to the list of durations
            if current_note in note_durations:
                durations.append(note_durations[current_note])
            # Reset the current note
            current_note = ''
        else:
            # Add the character to the current note
            current_note += char

    # Add the duration of the last note to the list of durations
    if current_note in note_durations:
        durations.append(note_durations[current_note])

    # Return the list of note durations
    return durations


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

Alternatively, here's a more concise version of the function:

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    notes = music_string.replace(' ', '')
    durations = []
    current_note = ''

    for char in notes +'':
        if char =='':
            if current_note in note_durations:
                durations.append(note_durations[current_note])
            current_note = ''
        else:
            current_note += char

    return durations


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```