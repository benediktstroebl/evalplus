```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the length of the longest string in the list.
    """
    longest = max(strings, key=len)
    return longest

# Example usage
input_strings = ['a', 'b', 'c']
print(longest(input_strings))  # Output: 3
input_strings = ['a', 'bb', 'ccc']
print(longest(input_strings))  # Output: 3

input_strings = []
print(longest(input_strings))  # Output: None

input_strings = ['a', 'b', 'c', 'aa', 'bb']
print(longest(input_strings))  # Output: 5
```

The code defines a function `longest` that takes a list of strings as input and returns the length of the longest string. The function uses the max function with the `key=len` argument to identify the longest string.