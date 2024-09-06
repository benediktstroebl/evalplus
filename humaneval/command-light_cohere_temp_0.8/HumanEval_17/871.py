```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    notes.py = ["". music_string is a string representing musical notes in a special ASCII format. The task is to parse this string and return a list of integers corresponding to how many beats does each note last. The function utilizes a legend: 
    - 'o' represents a whole note, lasting four beats
    - 'o|' represents a half note, lasting two beats
    - '.' represents a quarter note, lasting one beat

    >>> return [amount for symbol in music_string.replace where symbol in notes]
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    ```