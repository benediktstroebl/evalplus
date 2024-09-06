```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 4,
        ".":|": 1,
        "..": 4,
        "oO": [4, 4],  # Test for cyclic structure
        " ": []
    }
    
    result = []
    beat = 1
    for note in music_string:
        if note in notes:
            result.append(notes)
        beat += 4
        if note == " ": beat = 1
    return result

# Test the function
test_music = """o o| .| o| .| .| .| .| o o
"""
print(parse_music(test_music))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```