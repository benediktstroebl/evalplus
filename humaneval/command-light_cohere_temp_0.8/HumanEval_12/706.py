```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string.
    >>> longest(['a'])
    ValueError: Input list is empty
    """
    if not strings:
        raise ValueError("Input list is empty")
    return max(strings, key=len)

# Test cases
strings = ['a', 'bb', 'ccc']
longest(strings)  # Output: 'ccc'

strings = ['a']
try:
    longest(strings)
except ValueError as e:
    print(f"Error: {e}")

strings = []
try:
    longest(strings)
except ValueError as e:
    print(f"Error: {e}")

strings = ['a', 'bb', 'ccc']
longest(['a'])  # Output: 'a'

strings = ['ab', 'bc', 'ca']
longest(strings)  # Output: 'bc'
```

The above Python code defines a function `longest` that takes a list of strings as input and returns the longest string from the list. The `longest` function uses the `max` function with the `len` function as the key argument to get the length of each string in the list. The `test cases` section demonstrates how the function behaves with different inputs and helps to catch the edge case when the input list is empty.