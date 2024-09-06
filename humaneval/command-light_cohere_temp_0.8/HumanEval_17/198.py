```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ') '
   
    format = ['o', 'o|', '.|']
    notes = [int(x) for x in notes if x in format]
    return notes

# Test cases
test_cases = [
    "o o| .| o| .| .| .| .| o o",
    "oo",
    "oo ",
    "ooo",
    "oo o",
    " o o o o o",
    " o o|.",
    " o| o o o|.",
    " o o o| o o o|." ]

# Call the parse_music function with test cases
test_results = parse_music(test_cases)

# Print the test results
for result in test_results:
    print(result)
```
This script defines a function `parse_music` that parses a string representing music notes in a specific ASCII format. The function splits theator on space characters, converts the notes to integers, and then filters out the notes based on their format: 'o', 'o|', or '.|'. The test cases are then passed to the function, and the results are printed out.