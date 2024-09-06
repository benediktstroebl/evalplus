```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    :param strings: List of strings
    :return: Concatenated string
    """
    return ''.join(strings)

# Test case 1: empty list
print(concatenate([]))  # Output: empty string

# Test case 2: single string
print(concatenate('a'))  # Output: 'a'

# Test case 3: list of strings
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```
The function concatenate takes a list of strings as input and returns the concatenated string. It uses the example usage to test the function and print the output for different inputs.