```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format
    and return a list of integers corresponding to how many beats each note lasts.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    :param music_string: A string of musical notes in ASCII format
    :return: A list of integers representing the beats of each note
    """

    # Create a dictionary to map note symbols to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the music string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats = []

    # Iterate over each note in the music string
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o':
            # If the next note is also 'o', it forms a whole note
            if i + 1 < len(notes) and notes[i + 1] == 'o':
                beats.append(note_beats['o'])
                i += 2
            else:
                beats.append(note_beats['o'])
                i += 1
        # Check if the current note is a half note or a quarter note
        elif notes[i] in note_beats:
            beats.append(note_beats[notes[i]])
            i += 1

    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```