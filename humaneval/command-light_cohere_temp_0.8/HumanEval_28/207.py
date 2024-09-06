```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings
    Returns:
        string
    """
    return ''.join(strings)
# Example test cases
test_concat = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
assertEqual(concatenate(test_concat), 'abcdfgih')
test_empty = []
assertEqual(concatenate(test_empty), '')
test_single = 'a'
assertEqual(concatenate(test_single), 'a')

```
This code defines a function `concatenate` that takes a list of strings as an argument and returns a concatenated string. It uses the same strings to concatenate them and returns the result.

The test cases are also provided. You can add more test cases to solve more scenarios.