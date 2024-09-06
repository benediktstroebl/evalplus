```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    notes.ph specific notes to be string, with '|' acting as separator between the notes. The function splits the process string into a list of char arrays and then performs a regex replace operation on each array to extract the number of beats. The result is then a list comprehension to map the notes to the correct beat count.