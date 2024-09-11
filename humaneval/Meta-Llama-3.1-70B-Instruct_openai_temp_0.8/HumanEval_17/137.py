```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers
    representing the number of beats each note lasts.

    :param music_string: A string of musical notes in a special ASCII format.
    :return: A list of integers representing the number of beats each note lasts.
    """
    # Create a dictionary to map each note to its corresponding number of beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the number of beats for each note
    beats = []

    # Initialize an empty string to build each note
    note = ''

    # Iterate over each character in the music string
    for char in music_string:
        # If the character is a space, it means we've reached the end of a note
        if char =='':
            # If the note is not empty, look up its number of beats and add it to the list
            if note:
                beats.append(note_beats[note])
                note = ''
        else:
            # If the character is not a space, add it to the current note
            note += char

    # If the music string doesn't end with a space, we need to add the last note's beats to the list
    if note:
        beats.append(note_beats[note])

    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes in a special ASCII format and returns a list of integers representing the number of beats each note lasts. It uses a dictionary to map each note to its corresponding number of beats and iterates over the music string to build each note and look up its number of beats. The function handles notes that are not separated by spaces at the end of the music string.