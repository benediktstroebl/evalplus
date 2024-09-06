```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: list of strings to concatenate
    Returns:
    string
    """
    return ''.join(strings)

# Test the function with various inputs
strings = ['a', 'b', 'c']
result = concatenate(strings)
print(result)  # Output: 'abc'

strings = []
result = concatenate(strings)
print(result)  # Output: ''

strings = ['a', '123']
result = concatenate(strings)
print(result)  # Output: '123'
``` 
The code defines a function called `concatenate` that takes a list of strings as input and returns a concatenated string. The function uses the string `join` method to concatenate the strings in the list. The code then tests the string concatenation by passing different inputs to the function, and the expected output is printed to the console.