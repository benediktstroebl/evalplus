```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    notes_list = [notes.get(x) for he in music_string.replace(notes)]
    return notes_list
```
 This Python code defines a function named parse_music that takes a music_string containing notes in a special ASCII format as input. The function creates a dictionary of musical notes with their respective beat values. Then, it employs a list comprehension to extract the beat values of the notes from the input string and stores them in a new list. The output of the function is a list of integers representing the beat values of the notes in the music_string.