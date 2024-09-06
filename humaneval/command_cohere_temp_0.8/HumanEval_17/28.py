```python
from typing import List

PATTERN = "o|o|.|"

def parse_music(music_string: str) -> List[int]:
    result = []
    curr_note = 4

    for c in music_string:
        if c == 'o':
            curr_note *= 4
        elif c == '|':
            curr_note //= 2
        elif c == '.':
            result.append(curr_note)
            curr_note = 4
        else:
            raise ValueError(f"Unexpected char `{c}` in the music string")

    if curr_note != 4:
        result.append(curr_note)

    return result
``` 

This approach uses a "state machine" (the variables `curr_note` and `pattern`) to parse the string, which has some advantages:
- It is quite straightforward to add more parsing rules without making the code much more complicated.
- It's easier to validate if some input creates an unexpected state (e.g., a `TypeError` or `ValueError` will be raised immediately when this happens).
- It more cleanly separates the "beat-adding" behavior from the actual parsing, which means that if you later want to change the behavior (e.g., add an option for customizing the note lengths), you can do so without changing the part of the code that does the parsing.

However, the drawback is that it may need more memory than the previous "roll your own" solution, and might be a bit less straightforward to deploy to embedded devices or other such "low-memory" environments. It also is less straightforward to estimate the time complexity, since it depends on the input and how the state machine will evolve. With some analysis, you could likely estimate that it will take `O(n)` time and `O(n)` memory, but these are not necessarily optimal.