Here is a self-contained Python script that implements the longest function from the previous prompt:
```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Returns the length of the longest string.
    """
    def max_length(strings: List[str]) -> int:
        max_len = float('-inf')
        for string in strings:
            if len(string) > max_len:
                max_len = len(string)
        return max_len
    return max_length

# Test case
def test(func):
    longest_result = func([])
    assert longest_result is not None
    longest_length = func(['a', 'bb', 'ccc'])
    assert len(longest_length) == 3
```
The `longest()` function is defined with an input list of strings, and it returns the length of the longest string. The `max_length()` function calculates the maximum length of the string in the input list and returns the result.