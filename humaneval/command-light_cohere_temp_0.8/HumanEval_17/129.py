```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    notes_list = [notes.get(x, notes. main_string.get(note)
   
  note)
        for note in notes_list]
    return [note for note in music_string.parse(notes)]

```
This function uses a dictionary to map musical note characters to their respective beat values. The `get()` method is used to retrieve the beat value of a given note. The function also uses the string `parse()` method to split the input string into a list of characters, and then uses a list comprehension to convert those characters into the corresponding beat values.