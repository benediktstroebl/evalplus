```python
# Import the list module from the typing module
from typing import List


# Define the function that takes in a list of strings and returns a string
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    result = ''
    for string in strings:
        result += string
    return result


# Include examples from the problem statement
# Concatenate an empty list
>>> concatenate([])
''

# Concatenate a list of three strings
>>> concatenate(['a', 'b', 'c'])
'abc'
```

The `concatenate()` function accepts a list of strings and returns a single string. It iterates through the list, appending each string to an accumulating `result` variable. The empty list example tests an edge case, proving that the function handles it correctly by returning an empty string. Similarly, the three-string list example shows the function operating as expected, producing a concatenated string: 'abc'.