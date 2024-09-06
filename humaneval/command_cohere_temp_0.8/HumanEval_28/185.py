```python
# Import the necessary module
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

The `concatenate` function accepts a list of strings and returns a single string concatenated from the input list. The `typing` module is used to declare the input parameter as `List[str]` for type-checking purposes. You can readily use this function to concatenate strings efficiently. 

The provided tests ensure the function's correctness against edge cases and demonstrate its basic usage.