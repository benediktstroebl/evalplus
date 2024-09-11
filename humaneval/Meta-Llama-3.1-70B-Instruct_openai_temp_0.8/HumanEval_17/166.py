```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers 
    corresponding to how many beats each note lasts.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to how many beats each note lasts.
    """
    # Create a dictionary to map the musical notes to the number of beats they last
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the music string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the number of beats for each note
    beats = []

    # Iterate over each note in the music string
    i = 0
    while i < len(notes):
        # Check if the current note and the next one form a half or quarter note
        if i < len(notes) - 1 and notes[i] +'' + notes[i + 1] in ['o |', '. |']:
            # If they do, append the corresponding number of beats to the beats list
            beats.append(note_beats[notes[i] + '|' if notes[i] + '|' in note_beats else '.|'])
            # Skip the next note as it has already been processed
            i += 2
        else:
            # If they don't, append the corresponding number of beats to the beats list
            beats.append(note_beats[notes[i]])
            # Move on to the next note
            i += 1

    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```