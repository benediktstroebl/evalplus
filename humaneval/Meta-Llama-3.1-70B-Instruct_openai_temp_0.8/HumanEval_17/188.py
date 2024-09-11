```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    # Create a dictionary to map notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the music string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats = []

    # Iterate over each note
    i = 0
    while i < len(notes):
        # Check if the current note and the next note form a half or quarter note
        if i < len(notes) - 1 and notes[i] == 'o' and notes[i + 1] == '|':
            # If they do, append the beats of the half note to the list and skip the next note
            beats.append(note_beats['o|'])
            i += 2
        elif i < len(notes) - 1 and notes[i] == '.' and notes[i + 1] == '|':
            # If they do, append the beats of the quarter note to the list and skip the next note
            beats.append(note_beats['.|'])
            i += 2
        else:
            # If they don't, append the beats of the whole note to the list
            beats.append(note_beats[notes[i]])
            i += 1

    return beats


# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```