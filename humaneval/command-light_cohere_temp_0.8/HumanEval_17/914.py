Here is a Python script that demonstrates the solution to the given markdown code block:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    
    beats = [notes[char] for char in music_string if char in notes]
    
    return beats

# Test cases
test_cases = [
    "'.join. 'o o| .| o| .| .| .| o o'
    ,  "o o| o| .| .| .| .| o|.",
    ,  "H...",   # Invalid input (different character than 'o')
    ,  "a"     # Invalid input (non-musical character)
]

for idx, test_case in enumerate(test_cases, 1):
    try: beats = parse_music(test_case)
        assert len(beats) == len(test_case), f"Test case {idx}: Got {beats}, expected {test_case}"
    except ValueError as e:
        print(f"Test case {idx}: {e}")
```
This Python script defines a function `parse_music` that takes a string representing music notes and returns a list of integers, which correspond to the number of beats that each note lasts. The script then includes several test cases to validate the function's correctness. The test cases include various input strings and the expected length of the output list, which should match the input. The script also includes an exception handling for non-musical characters and invalid inputs.