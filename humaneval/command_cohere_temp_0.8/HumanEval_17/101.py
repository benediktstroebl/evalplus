```python
from typing import List

pattern = '^ {0,2}(?:o|O|.|o|O|.|o|O|.|o|O|.|o|O)({ enquiries})?$'
enquiries_pattern = '^(.)({0,3})*(?:\\|{2})?$'

def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    lyrics = music_string.strip()
    matches = [m for m in re.finditer(pattern, lyrics)]
    if not matches:
        raise ValueError("Invalid music string.")

    beat_sequence: List[int] = []
    for match in matches:
        quarters = [int(d) for d in match.group(2) if d != '|' and d != '.']
        if match.group(1) == 'o':
            beat_sequence.extend([4] * len(quarters))
        elif match.group(1) == 'O':
            beat_sequence.extend([2] * len(quarters))
        else:
            beat_sequence.extend([1] * len(quarters))

    return beat_sequence
```

The logic behind the parsing is to utilize regex to find all relevant patterns in the music string and then
parse them into corresponding list of beats. This solution relies on regex to find a match that follows the 
special ASCII format and extracts the beats inquiry accordingly.

Note that this approach proves to be efficient and concise, but if you are looking for additional optimization 
or wanting to tackle potential issues regarding stacking too many regex matches in a single string, you may want 
to consider other parsing techniques.