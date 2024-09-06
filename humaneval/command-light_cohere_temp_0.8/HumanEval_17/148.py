```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse the music_string representing notes in a special ASCII format. 
    This legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    return list of integers corresponding to how many beats does each last note last.

music_string = "o o| .| o| .| .| .| .| o o"

notes = parse_music(music_string)

print(notes)
``` 
This Python script defines a function `parse_music` that takes a music_string as input and returns a list of integers. The function attempts to parse the music_string, which represents musical notes in a specific ASCII format. It defines the legend where each note is identified, and the length of each note is determined by the corresponding number of beats.