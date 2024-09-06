Here's a self-contained Python script with a function that parses markdown code and handles the given problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
        }
    
    beat_count = len(music_string) // 4
    
    result = [beat_count] * notes[music_string[0]]
    for i in range(1, len(music_string)):
        if music_string[i] in notes:
            result[beat_count] += notes[music_string[i]]
        else:
            result[-1] += 1
    
    return result

# Example test cases
test_cases = [
    "o o| .| o| .| .| .| .| o o",
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4],
    "o o| .| o| .| .| .| .| .| o",
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 2, 1],
]

for case in test_cases:
    print(parse_music(case))
``` 
This code defines a parse_music function that takes a music string in markdown format as input and returns a list of beat counts. It uses a expected values and a dictionary to interpret the markdown syntax. The code then demonstrates the structure and functionality by using test cases.