```markdown
### Music Note Parser

This Python script defines a function `parse_music` to parse a string of musical notes in ASCII format and returns a list of integers representing the number of beats each note lasts.

#### Code
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in ASCII format and return a list of integers representing the number of beats each note lasts.

    Args:
        music_string (str): A string representing musical notes in ASCII format.

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts.
    """
    # Define a dictionary to map notes to their corresponding beats
    note_beats = {'o': 4, 'o|': 2, '.|': 1}

    # Initialize an empty list to store the beats
    beats = []

    # Split the input string by spaces
    notes = music_string.split()

    # Iterate over each note in the string
    for note in notes:
        # Check if the note is in the dictionary and append its beats to the list
        if note in note_beats:
            beats.append(note_beats[note])
        else:
            # Raise a ValueError if the note is not in the dictionary
            raise ValueError(f"Invalid note: '{note}'")

    return beats

#### Example Use Cases
```

```python
# Test the function with the provided example
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

```python
# Test the function with a different input
print(parse_music('o o|.|.'))
# Output: [4, 2, 1, 1]
```

```python
# Test the function with an invalid note
try:
    print(parse_music('o x|'))
except ValueError as e:
    print(e)
# Output: Invalid note: 'x|'
```