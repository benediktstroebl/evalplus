```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Returns: string concatenation of provided strings"""
    return ''.join(strings)

# Test case: empty list
print(concatenate([])) # Output: ''

# Test case: single string
print(concatenate('a')) # Output: 'a'

# Test case: list of strings
print(concatenate(['a', 'b', 'c'])) # Output: 'abc'
```
This code defines a function `concatenate` that takes a list of strings as input and concatenates them into a single string. It then prints the+ output of the function with the given test cases, successfully demonstrating the functionality.

You can use this function in your markdown code block to get the desired result.