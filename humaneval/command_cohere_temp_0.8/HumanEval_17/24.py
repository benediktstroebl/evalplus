```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    mod = 4  # whole note lasts 4 beats
    beats = []

    current_beat = 0
    for char in music_string:
        if char == 'o':
            current_beat += mod
        elif char == '|':
            current_beat += mod // 2
        elif char == '.':
            beats.append(current_beat)
            current_beat = 0
        else:
            raise ValueError("Invalid input")

    if current_beat > 0:
        beats.append(current_beat)

    return beats
```

The algorithm works by simply counting the number of beats based on the ASCII diagram provided. It iterates over each character in the `music_string`, and adds the appropriate number of beats to the current beat count. When it encounters a '.' it saves the current beat count and resets the beat count to 0, since the next note starts fresh. The beat count accumulates again until the next '.' is reached.

To ensure the algorithm handles all test cases correctly, it also checks for an additional '.' at the end of the input string, since the last note might not end at the line boundary. 

The code is type-safe due to the usage of the `typing` module, and uses a constant `mod` variable to reduce redundancy. Despite the fact the function is not the fastest (it runs in `O(n)` where `n` is the length of the input string), it is clear, concise, and easy to understand, which is a priority in this case.