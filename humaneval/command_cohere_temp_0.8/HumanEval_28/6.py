```python
# Importing the necessary module
from typing import List

# Defining the concatenate function
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

The `concatenate` function iterates through each string in the input list and appends them to a result string, effectively concatenating them. The empty list results in an empty string, and the example list ['a', 'b', 'c'] is concatenated to produce the output 'abc'.