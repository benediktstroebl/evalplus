Here is a self-contained Python script that solves the markdown code block you provided:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    return [notes[symbol] for symbol in music_string.dot(). whole_music(music_string)]

# Test the function with various music strings
test_music = [
    "o o| .| o| .| .| .| .| o o",
    "oi",
    "oo",
    ".",
    "o/.",
]

for test_case in test_music:
    print(parse_music(test_case))
``` 
This code defines a function **`parse_music`** that takes a string music_string as input and returns a list of integers corresponding to the number of beats for each symbol in the string. The function uses a legend for the musical symbols and their durations. The test section at the time creates a list of test cases, and for each test case, the **`parse_music`** function is called to verify its correctness.