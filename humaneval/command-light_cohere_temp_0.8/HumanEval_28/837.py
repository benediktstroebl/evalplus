```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""

    return ''.join(''.join(strings) if strings else '')

# Test cases
test_cases = [
    [],  # Empty list
    ['a'],  # Single string
    ['a', 'b', 'c'],  # Three strings
    ['a', 'b', 'ccc'], # Extra "ccc" shouldn't affect the result
    ]

for test_case in test_cases:
    print(concatenate(test_case))  # Output should be "abc"
``` 
The provided code defines a function `concatenate` that takes a list of strings as input and concatenates them into a single string. It uses the basic string concatenation `'.join` and checks if the input list is empty, it returns an empty string, otherwise, it concatenates all the strings.

The code also includes a set of test cases, which are passed to the `concatenate` function to test its correctness.