```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers.
    Each integer in the list corresponds to the duration of the note in beats.

    :param music_string: A string of musical notes
    :return: A list of integers representing the duration of each note in beats
    """

    # Define a dictionary to map each note to its duration
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the music string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the note durations
    durations = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the music string
    for char in music_string:

        # Add the character to the current note
        current_note += char

        # Check if the current note is in the note_durations dictionary
        if current_note in note_durations:

            # If it is, add its duration to the durations list
            durations.append(note_durations[current_note])

            # Reset the current note
            current_note = ''

    return durations


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

However, there is a cleaner and more Pythonic way of solving this problem by splitting the string into notes and then using a dictionary to map each note to its duration:

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers.
    Each integer in the list corresponds to the duration of the note in beats.

    :param music_string: A string of musical notes
    :return: A list of integers representing the duration of each note in beats
    """

    # Define a dictionary to map each note to its duration
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the music string into individual notes
    notes = music_string.split()

    # Use a list comprehension to create a list of note durations
    durations = [note_durations[note] for note in notes]

    return durations


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This solution assumes that the input string is well-formed and does not contain any invalid notes. If the input string can contain invalid notes, you should add error checking code to handle this.