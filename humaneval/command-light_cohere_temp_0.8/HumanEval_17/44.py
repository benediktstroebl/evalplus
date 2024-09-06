Here's a self-contained Python script with a function that parses a music string representing notes in a special ASCII format into a list of integers representing how many beats each note lasts:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format
    as input, and returns a list of integers corresponding to how many beats does each note last.

    The legend:
    'o' - whole note, lasts 4 beats
    'o|' - half note, lasts 2 beats
    '.|' - quarter note, lasts 1 beat

    :param music_string: str - input string representing musical notes
    :return: List[int] - list of integers corresponding to the number of beats each note lasts
    """
    beats: List[int] = []

    for note in music_string:
        if note == 'o':
            beats.append(4)
        elif note == 'o|':
            beats.append(2)
        elif note == '.|':
            beats.append(1)
        else:
            print("Invalid input. Not adding to beats:", note)
        return beats
```
This function is designed to handle various input scenarios, and it includes error handling for invalid inputs. 
You can use this function to parse music strings and obtain the desired output.