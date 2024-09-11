```markdown
### Solution: parse_music Function

The `parse_music` function parses a string representing musical notes and returns a list of integers corresponding to the number of beats each note lasts.

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes and return a list of integers corresponding to the number of beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to the number of beats each note lasts.

    """
    # Define a dictionary to map each note to its corresponding number of beats
    note_beats = {'o': 4, 'o|': 2, '.|': 1}

    # Initialize an empty list to store the number of beats for each note
    beats = []

    # Initialize an empty string to store the current note
    current_note = ''

    # Iterate over each character in the music string
    for char in music_string:
        # If the character is a note, add it to the current note
        if char in note_beats:
            current_note += char
        # If the character is not a note, it's a delimiter, so add the current note to the list of beats
        else:
            # If the current note is not empty, add its beats to the list
            if current_note:
                beats.append(note_beats[current_note])
                current_note = ''

    # If the music string ends with a note, add its beats to the list
    if current_note:
        beats.append(note_beats[current_note])

    return beats

# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines the `parse_music` function, which takes a string representing musical notes as input and returns a list of integers corresponding to the number of beats each note lasts. It uses a dictionary to map each note to its corresponding number of beats and initializes an empty list to store the number of beats for each note. The function iterates over each character in the music string, adding notes to the current note string and adding the current note to the list of beats when it encounters a delimiter. Finally, it returns the list of beats. The example usage demonstrates how to use the `parse_music` function to parse a string representing musical notes.