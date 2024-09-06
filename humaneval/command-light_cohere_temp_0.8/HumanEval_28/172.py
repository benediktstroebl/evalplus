```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: list of strings
    Returns:  string
    """
    return ''.join(strings)

# test
my_strings = ['a', 'bcde', 'abc', 'a']
print(concatenate(my_strings))  # Output: abcdeabc
``` 
This script defines a function `concatenate` that takes a list of strings and concatenates them into a single string. It uses the string formatting to return the concatenated string.