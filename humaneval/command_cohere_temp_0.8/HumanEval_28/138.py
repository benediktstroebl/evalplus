```python
# Importing required module
from typing import List


# Define the function
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    result = ''
    for string in strings:
        result += string
    return result


# Example usage
>>> concatenate([])
''
>>> concatenate(['a', 'b', 'c'])
'abc'
```

This script defines a function called `concatenate` that takes a list of strings as input and returns a single string as output. It runs through each string in the provided list and adds them together to form one concatenated string, effectively combining all the given strings into one. 

The example usage demonstrates how to utilize the `concatenate` function correctly, resulting in an empty string when an empty list is passed and the expected 'abc' when the list ['a', 'b', 'c'] is passed.