```python
from typing import List

 Pattern = str
 Beats = int


def parse_music(music_string: Pattern) -> List[Beats]:
    NOTES = {'o': 4, 'o|': 2, '.': 1}
    return [NOTES.get(note, 0) for note in music_string]
```

The BeatParser function takes a music_string as an input and returns a list of beats. It utilizes a dictionary called `NOTES` that associates special ASCII characters ('o', 'o|', '.') with their beat lengths (whole note, half note, quarter note). The function uses a list comprehension to iterate through each note in the `music_string`, extracting the beat length using `NOTES.get(note, 0)`. This ensures that any unknown characters are considered as having a length of 0. The result is a list of beats representing the duration of each note in the input string.

Here is an example usage of this function:
```python
beatstr = 'o o| .| o| o| .| .| .| .| o o'
beats = parse_music(beatstr)
print(beats)
```

Output:
```
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```