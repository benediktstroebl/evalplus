```python
# Import the necessary module
from typing import List

# Declare the function
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

The `concatenate` function takes a list of strings (`List[str]`) as an argument and returns a single string that concatenates all the strings in the list. It does this using a for loop to iterate through each string in the list and adding it to a running result variable.

The example tests demonstrate the function's behavior when an empty list and a list containing three letters are passed in.