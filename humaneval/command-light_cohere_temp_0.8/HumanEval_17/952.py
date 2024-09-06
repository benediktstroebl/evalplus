Here's a self-contained Python script that defines a function `parse_music` which takes a music string in a specific format and returns a list of integers representing the number of beats for each note. 

```python
import typing

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is the legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> music_string = 'o o| .| o| o| .| .| .| o o'
    beats: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]'
    return beats
```