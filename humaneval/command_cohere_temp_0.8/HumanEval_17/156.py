```python
from typing import List

 Pattern = str


def parse_music(music_string: Pattern) -> List[int]:
    beat_lengths = {
        "o": 4,
        "o|": 2,
        ".|": 1,
    }

    return [beat_lengths[note] for note in music_string]
```

The beat_lengths dictionary assigns musical notation to their corresponding beat lengths. The function iterates through each character in the `music_string`, extracting its beat length from the beat_lengths dictionary and returning the result as a list.

This solution does not require any external dependencies or additional modules and is suitable for the problem that needs to be solved. It is very concise and readable, and efficient with time and memory with the `beat_lengths` dictionary for mapping.