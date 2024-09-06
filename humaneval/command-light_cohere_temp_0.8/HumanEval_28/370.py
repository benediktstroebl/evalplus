```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    
    Returns:
        str: Concatenated string
    """
    return ''.join(strings)

# Test cases
strings = ["a", "b", "c"]
result = concatenate(strings)
print("Result:", result)

strings = []
result = concatenate(strings)
print("Result:", result)

strings = ["a", "abc"]
result = concatenate(strings)
print("Result:", result)

strings = ["abc", "a"]
result = concatenate(strings)
print("Result:", result)
```
The provided code defines a function `concatenate` that takes a list of strings as input and concatenates them into a single string. It uses the dry typing with string literals (`''`) to create a string and then joins the strings in the list using the `join` method. The test cases demonstrate the dry typing with empty strings, which should return an empty string, and concatenating strings of different lengths, which should result in a correctly formatted string.