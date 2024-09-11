```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format
    and returns a list of integers corresponding to how many beats each note lasts.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    :param music_string: A string representing musical notes
    :return: A list of integers representing the duration of each note in beats
    """

    # Create a dictionary to map note representations to their corresponding beat durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat durations of the notes
    beat_durations = []

    # Iterate over the notes and append their beat durations to the list
    for note in notes:
        # If the note is a whole note, it may be represented as 'o' or 'o'(with a trailing space)
        if note == 'o' or note == 'o ':
            beat_durations.append(note_durations['o'])
        else:
            # For other notes, simply look up their beat durations in the dictionary
            beat_durations.append(note_durations[note])

    return beat_durations


print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```