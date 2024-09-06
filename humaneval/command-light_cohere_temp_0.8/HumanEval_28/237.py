```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings
    Returns:
        string
    """
    return ''.join(strings)

# Test the function
strings = ['a', 'bcde', 'abc']
result = concatenate(strings)
print(result) # Output: 'abcdeabc'
```
The given Python script defines a function `concatenate` that takes a list of strings as an argument and returns the concatenation of these strings as a single string. It then tests theink with a list of test strings and prints the result, which passes all the tests.