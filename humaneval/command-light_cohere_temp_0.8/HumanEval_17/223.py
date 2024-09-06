Here is a self-contained Python script that defines a function `parse_music` solving the problem of parsing a music note representation and returning a list of corresponding beats:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    >>>
    Music string example:
    'o o| .| o| .| .| .| .| o o'
    
    Returns: 
    list of numbers, where each number represents the number of beats for its corresponding note.
    """
    pattern: 
    ''.join - whole note
    'o' - half note
    'o|' - quarter note
    '.' - rest note
    [4, 2, 1, 2, 2, 1, 1, 1, 4]
    """
    # Define all possible notes
    notes = ['o','.',o','.','.', 'o','.|', '.'o','.|']

    # Initialize a counter to keep track which note is playing and how many beats have been played
    counter = [0] * len(notes)

    # Loop through the music string
    for note in music_string:
        # If the note is a whole or half note
        if note in notes:
            counter[notes.index(note)] += 1
        # If the note is a rest, just add 1
        else:
            counter[-1] += 1

    return counter
```