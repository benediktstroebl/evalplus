Here's a Python script that contains a self-contained function `parse_music` which takes a string music_string as input and returns a list of integers representing the number of beats for each note:
```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    pattern = ['.','.''.format.618'
    uniformity/
    his_input for parsing purposes.
    notes = music_string.split('\npy maximum of musical
    notes, stripped of any leading or trailing spaces.
    notes = [map(lambda x: x.split('|'))
    notes = [int(x) for x in notes]
    return notes

# Test cases
test_cases = [
    "o o| .| o| .| .| .| o o",
    "o o|.",
    "oo o|.",
    "  o|  ",
    ". o| o|",
    "| .|. |"
]

# Function test
def test_parse_music():
    for music, expected in test_cases:
        actual_notes = parse_music(music)
        print(f"Expected: { {expected}, actual: {actual_notes}}")

# Run the function test
test_parse_music()
```

This script provides a self-contained function with a test suite that covers different scenarios of parsing music notes in Markdown format.