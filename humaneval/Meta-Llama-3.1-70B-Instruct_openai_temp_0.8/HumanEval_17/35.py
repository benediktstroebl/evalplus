```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers.
    Each integer in the list represents the number of beats a corresponding note lasts.

    :param music_string: A string of musical notes.
    :return: A list of integers representing the number of beats each note lasts.
    """

    # Create a dictionary to map notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the music string into a list of notes
    notes = music_string.split()

    # Initialize an empty list to store the beats
    beats = []

    # Iterate over each note in the list of notes
    i = 0
    while i < len(notes):
        # Check if the current note and the next note together form a note with a bar
        if i < len(notes) - 1 and notes[i] == 'o' and notes[i + 1] == '|':
            # If they do, append the beats for the note with a bar to the list
            beats.append(note_beats['o|'])
            # Skip the next note
            i += 2
        elif i < len(notes) - 1 and notes[i] == '.' and notes[i + 1] == '|':
            # If they do, append the beats for the note with a bar to the list
            beats.append(note_beats['.|'])
            # Skip the next note
            i += 2
        else:
            # If they don't, append the beats for the current note to the list
            beats.append(note_beats[notes[i]])
            # Move to the next note
            i += 1

    # Return the list of beats
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```