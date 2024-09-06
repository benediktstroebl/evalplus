```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    :param strings: list of strings to concatenate
    :return: concatenated string
    """
    return ''.join(strings)

# Test cases
print(concatenate(['a', 'b', 'c'])) # Output: 'abc'
print(concatenate(['']) ) # Output: ''
print(concatenate(['a', '', 'b', 'c'])) # Output: 'abc'
print(concatenate(['a', ' '])) # Output: 'a '
print(concatenate(['abcde', 'fghijk'])) # Output: 'abcdefghijk'
```
This function takes a list of strings and returns a new string by concatenating them. 
The test cases validate that the function works correctly with different inputs.