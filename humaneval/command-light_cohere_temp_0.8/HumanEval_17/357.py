Here's the self-contained Python function that solves the problem:
```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ') | [' '.join(note for note in notes) if note != '']
    return [len(notes) for notes in [notes, notes[::-1], notes[1:], notes[:-2]]
```
The function splits the music_string into a list of notes separated by '|'. It then iterates through each note, and creates a new list of the lengths of each note. It uses list comprehension and the generalizing the task to a list comprehension to handle all the input variations, which makes the function self-contained and easier to test.

The function also uses the split(' ') to split the music_string into a list of notes, which are then joined using the join(' '.join(note for note in notes) if note != ''') method. This allows the copious input strings into the function without the need for an additional separator.