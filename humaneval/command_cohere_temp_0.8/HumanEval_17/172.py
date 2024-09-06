```python
from typing import List

beats = {'o': 4, 'o|': 2, '.|': 1}

def parse_music(music_string: str) -> List[int]:
    result = []
    notes = music_string.strip().split('|')
    for n in notes:
        result += [beats[c] for c in n if c in beats]
    return result
```

The problem involves parsing a string representing musical notes in a special ASCII format and converting it into a list of integers representing the number of beats for each note. The input string contains a combination of 'o', 'o|', and '.|' characters, each representing a whole note, half note, and quarter note respectively. The beat durations are predefined in the beats dictionary.

The provided Python script offers a concise solution using string manipulation and the dictionary lookup technique. By splitting the input string into segments based on the '|'-character, and using the dictionary to look up the beat duration for each note type, the code efficiently computes the list of beat durations for each note in the input string. The result is a list of integers, properly typed for further usage.