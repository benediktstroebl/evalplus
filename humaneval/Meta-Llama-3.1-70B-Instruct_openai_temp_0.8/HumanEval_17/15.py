```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    :param music_string: A string representing musical notes
    :return: A list of integers representing the duration of each note in beats
    """
    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the duration of each note
    durations = []

    # Iterate over each note in the input string
    for note in notes:
        # Check the type of the note and append its duration to the list
        if note == 'o':
            durations.append(4)
        elif note == 'o|':
            durations.append(2)
        elif note == '.|':
            durations.append(1)

    # Return the list of durations
    return durations


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

Alternatively, you could use a dictionary to map the notes to their durations, which makes the code more concise:

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    # Define a dictionary to map the notes to their durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes and map each note to its duration
    durations = [note_durations[note] for note in music_string.split()]

    # Return the list of durations
    return durations


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```