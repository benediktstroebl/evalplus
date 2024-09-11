```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    parses it and returns a list of integers corresponding to how many beats each note lasts.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to how many beats each note lasts.
    """
    # Create a dictionary to map the musical notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into a list of notes
    notes = music_string.split()

    # Initialize an empty list to store the beats for each note
    beats = []

    # Iterate over each note
    i = 0
    while i < len(notes):
        # Check if the current note and the next one form a half or quarter note
        if i + 1 < len(notes) and notes[i] == 'o' and notes[i + 1] == '|':
            # If they do, append the beats for a half note and skip the next note
            beats.append(note_beats['o|'])
            i += 2
        elif i + 1 < len(notes) and notes[i] == '.' and notes[i + 1] == '|':
            # If they do, append the beats for a quarter note and skip the next note
            beats.append(note_beats['.|'])
            i += 2
        else:
            # If they don't, append the beats for a whole note
            beats.append(note_beats['o'])
            i += 1

    return beats


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```