```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    
    Returns:
        str: Concatenated string
    """
    return ''.join(strings)

# Test the function
test_strings = ['a', 'b', 'c']
result = concatenate(test_strings)
assert result == 'abc'
```
The provided code defines a function called `concatenate` which takes a list of strings as an argument and returns the concatenated string. The function uses the's `List[str]` syntax to accept the strings argument, which is a list of strings to be concatenated. The `return ''.join(strings)` expression is used to return the concatenated string.

The code also provides a test case for the `concatenate` function by creating a test list `test_strings` that contains the strings 'a', 'b', and 'c'. The `result` variable is assigned the result of the `concatenate` function, and the assert statement is used to check if the result is equal to the expected concatenated string 'abc'.