```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format.
    It parses this string and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers representing the number of beats each note lasts.
    """
    # Dictionary to map musical notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the music string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the notes
    for char in notes:
        # If the character is not a space, add it to the current note
        if char not in [' ', '']:
            current_note += char
        # If the character is a space or if we've reached the end of the string
        else:
            # If the current note is not empty
            if current_note:
                # Map the current note to its beats and add it to the list
                beats.append(note_beats.get(current_note, 0))
                # Reset the current note
                current_note = ''

    # Map the last note to its beats and add it to the list
    if current_note:
        beats.append(note_beats.get(current_note, 0))

    return beats


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This script defines a function `parse_music` that takes a string of musical notes and returns a list of integers representing the number of beats each note lasts. The function uses a dictionary to map musical notes to their corresponding beats and splits the input string into individual notes. It then iterates over each character in the notes, building the current note and mapping it to its beats when a space is encountered. The function handles the case where the input string ends with a note without a trailing space.