Here's the solution that fulfills the requirements:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split('|')
    string_notes = [note.split('o open')[0] for note in notes]
    return [int(len(string_notes[i])) for i in range(len(string_notes))]
```
This function splits the input string into a list of notes, then splits each note into its length and an optional rest (bar line). The function then iterates through each note, extracting the length, and returns a list of those lengths corresponding to the number of beats in each note.