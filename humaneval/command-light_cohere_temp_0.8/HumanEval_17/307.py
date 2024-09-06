Here's the Python script that implements the parse_music function, which is designed to parse a music notation string and return the number of beats for each note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    >>>
    [start_beat, end_beat] = map(int, music_string.split("o whole note|halfnote|quarternote"))
    return [start_beat, end_beat]
``` 
This function uses the map function to split the music_string into the character and its corresponding beat. Then, it uses the split function again to split the character into a whole note, a half note, or a quarter note, depending on the character. The beat numbers start from 0 for whole notes and decrease for half notes, and decrease even further for quarter notes.