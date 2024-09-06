```python
from typing import List

pattern = 'o|^.-^|O|X|-.|>'

def parse_music(music_string: str) -> List[int]:
    # Regular expression pattern matching table
    # Each char corresponds to a note length
    NOTE_PATTERN = 'o|^.-^|O|X|-.|'
    beat_lengths = {c:n for n,s in enumerate(NOTE_PATTERN, 1) for c in s}

    return [beat_lengths[c] for c in music_string]
```

Here is an example usage of the code:
```python
print(parse_music(pattern))
```

And here is the provided code with some comments to explain it:
```python
from typing import List

# Sample input pattern
pattern = 'o|^.-^|O|X|-.|>'

def parse_music(music_string: str) -> List[int]:
    # Regular expression pattern matching table
    # Each char corresponds to a note length
    NOTE_PATTERN = 'o|^.-^|O|X|-.|'
    beat_lengths = {c:n for n,s in enumerate(NOTE_PATTERN, 1) for c in s}

    return [beat_lengths[c] for c in music_string]
```

This approach utilizes a regular expression pattern (NOTE_PATTERN) to generate a dictionary mapping each 
relevant character to its corresponding beat length. The parsing function then utilizes this dictionary 
to determine the length of each note. It is important to note that this solution is specific to the 
provided input format and may not work correctly with different note patterns.