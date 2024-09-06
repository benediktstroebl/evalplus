```python
# Importing required module
from typing import List


# Defining the function
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    result = ''
    for string in strings:
        result += string
    return result


# Testing the function with examples
>>> concatenate([])
''

>>> concatenate(['a', 'b', 'c'])
'abc'
```

The `concatenate` function takes a list of strings as an argument and returns a single string as the result. It provides an empty string if the input list is empty, and concatenates each string in the list if it is not. This functionality is demonstrated through the test cases provided in the code.