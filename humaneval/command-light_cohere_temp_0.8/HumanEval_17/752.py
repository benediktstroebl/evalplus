Here is a self-contained Python function that solves the problem you described:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split('|')
    whole_note = int(note.split('o template')[0] * 4
    whole_note += (len(note.split('template')[0]) -1) * 2 if note.template else whole_note //1

    return [whole_note] + [note] for note in notes
```
The function parses the input string, which is a music note template represented as a string. The function splits the music_string into individual notes using the split('|') method, and then iterates through the notes. Then, the function calculates the note duration using the appropriate template and adds the note as a single beat. The final list of notes is returned.