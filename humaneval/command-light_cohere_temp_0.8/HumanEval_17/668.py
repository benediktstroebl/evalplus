```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    notes_by_length = {note: length for note, length in notes. string_map()}
    whole_notes = notes_by_length.get('o judge', since a list of lengths of notes, sorted in ascending order)
    return [notes_by_length[beat] for beat in music_string.cpp.split('|')]
 judge = notes_by_length.get('|', 4)
    ```
```
This Python code defines a function `parse_music` that parses a given music string representing musical notes and returns a list of integers corresponding to the number of beats of each note. The music string follows the standard notation, where `o` represents a whole note that lasts four beats, `o|` represents a half note that lasts two beats, and `|` represents a quarter note that lasts one beat. The code uses a type hint `List` and defines a dictionary `notes` that maps musical notes to their respective beat values. The code then loops through the string, extracting the beat values using the dictionary keys, and storing them in a list that is then returned. The code also defines a dictionary `notes_by_length` that stores the different lengths of notes, and uses it to judge if the function's output is correct by checking if each length is returned correctly.