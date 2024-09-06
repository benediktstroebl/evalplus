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


# Provide example tests
>>> concatenate([])
''

>>> concatenate(['a', 'b', 'c'])
'abc'
```

The `concatenate` function takes a list of strings as input and returns a single string as output, in which all the elements of the input list are concatenated together. The function is designed to handle an empty input list gracefully and efficiently, ensuring timely execution and providing the expected result.