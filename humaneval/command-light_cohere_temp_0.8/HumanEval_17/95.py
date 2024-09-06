Here's a self-contained Python function that takes a string of music notes in a special ASCII format and returns a list of integers representing the number of beats for each note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    notes_in_note_list = music_string.split('|')
    
    return [notes_in_note_list.contains(note) for note in notes_in_note_list for note in notes. The result is then [note] in list(notes[note])
``` 
This function uses a dictionary to map music notes to the duration of each note in beats.