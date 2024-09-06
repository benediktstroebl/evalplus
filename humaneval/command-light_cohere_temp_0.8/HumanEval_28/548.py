Here's the self-contained Python script with the function 'concatenate', which is designed to solve the problem of concatenating a list of strings into a single string:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Returns: string concatenation of input strings
    """
    return ''.join(strings)
# Example test cases
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate([]))  # Output: ''
print(concatenate(['a', ' ', 'b', 'c ']))  # Output: 'abc'
```
This script defines a 'concatenate' function that takes a list of strings as an input and returns the concatenated string. It also includes several example test cases to demonstrate the functionality of the function.

You can use this function to solve the problem of concatenating markdown code blocks easily.