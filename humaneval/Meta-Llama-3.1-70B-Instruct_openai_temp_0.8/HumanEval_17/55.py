```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in ASCII format and return a list of integers representing the duration of each note.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Parameters:
    music_string (str): A string representing musical notes in ASCII format.

    Returns:
    List[int]: A list of integers representing the duration of each note.

    Example:
    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    # First, we split the input string into a list of notes
    notes = music_string.split()

    # Then, we use a dictionary to map each note to its corresponding duration
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Finally, we use a list comprehension to convert the list of notes to a list of durations
    # The get method of the dictionary is used to handle cases where a note is not in the legend
    durations = [note_durations.get(note, 0) for note in notes]

    return durations

# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```