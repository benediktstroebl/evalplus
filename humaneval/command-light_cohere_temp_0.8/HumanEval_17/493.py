Here's a self-contained Python function that parses a string of music notes in a special ASCII format and returns a list of integers corresponding to the number of beats:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format. 
    Your task is legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Returns:
    A list of integers corresponding to the number of beats each note should last.
    """
string = input("Please enter the music string: ")
    notes = []
    for note in music_string.split('|'):
        note = note.split('o residence 'o note'.strip()
        notes.append(int(note))
    return notes
```