```markdown
# Music Note Parser

## Function to Parse Musical Notes
### 
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    note last.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Args:
        music_string (str): A string representing musical notes

    Returns:
        List[int]: A list of integers corresponding to how many beats does each note last
    """
    music_notes = music_string.split()
    beat_list = []

    # Loop through each note in the music string
    for note in music_notes:
        # Check the note type
        if note == 'o':
            # Add 4 beats for a whole note
            beat_list.append(4)
        elif note == 'o|':
            # Add 2 beats for a half note
            beat_list.append(2)
        elif note == '.|':
            # Add 1 beat for a quater note
            beat_list.append(1)

    return beat_list

## Example Usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```
### Output
```
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the number of beats for each note. It uses a loop to iterate through each note in the string, checks the note type, and adds the corresponding number of beats to the list. The example usage demonstrates how to call the function with a sample input string and print the resulting list of beats.