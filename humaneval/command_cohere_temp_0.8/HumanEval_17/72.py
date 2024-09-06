```python
from typing import List

 Patterns = {
    'o': 4,
    'o|': 2,
    '.|': 1,
}


def parse_music(music_string: str) -> List[int]:
    result = []
    curr_beat = 0
    for note in music_string:
        if note in Patterns:
            curr_beat += Patterns[note]
            result.append(curr_beat)
        elif note == '|':
            curr_beat = 0
    return result
```

The beat parser works by checking each character of the music string against the dictionary of predefined beat patterns. When it encounters a known beat pattern, it adds the beat value from the patterns dictionary to the current beat value on the fly. Additionally, when it encounters a "|"-character, it resets the current beat value to zero, ensuring that each new beat starts counting from zero. This way, it accurately computes the beats of each note in the provided music string.