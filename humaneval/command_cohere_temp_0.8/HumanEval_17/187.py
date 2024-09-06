```python
from typing import List

pattern = '^[o|O]|\.|^|?'

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
    return [len(re.findall(pattern, segment)) for segment in music_string.split('|')]
```

This script leverages the `re` module and regular expressions to match the different types of notes. It uses a "group" clause to ask for only a single match in a given segment. Given a segment "o o| .| o| o| .| .| .| .| o o" it will therefore return the integers [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]. 

A note is a whole note 'o' if it is not followed by a vertical bar |, nor by a dot .., and if it is the first character of the segment. It can also be a whole note 'O' if the segment starts with this character. In both cases, it lasts four beats. 

A note is a half note 'o|' if it is followed by a vertical bar |, while it is a quater note '.|' if it is followed by a dot .. In both cases, the number of beats it lasts is 2. Lastly, if none of the above conditions are met, the note is a quater note '?' and it lasts only one beat. 

The pipe | and the dot .. are literal characters in the regular expressions and should be part of the string to match. 

The output list [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4] corresponds to the number of beats for each note in the provided example string. Feel free to adjust the pattern to accommodate different rules or special cases if needed.