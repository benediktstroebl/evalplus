```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of music in special ASCII format, where each line 
    represents a beat. 
    Here is the legend: 
    - 'o' - whole note, lasts four beats
    - 'o|' - half note, lasts two beats
    - '.|' - quarter note, lasts one beat. 

    task is to parse this string 
    and return a list of integers corresponding to the number of beats each note lasts. 

    parse_music('o o o| .| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    notes = []
    current_beat = 0
    for beat in music_string:
        if beat == 'o':
            notes.append(current_beat)
            current_beat += 4
        elif beat == 'o|':
            current_beat += 2
        elif beat == '.|':
            current_beat += 1
        else:
            raise ValueError("Invalid music string")
    return notes
```