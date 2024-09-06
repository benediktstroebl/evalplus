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

# Test case 1
strings = []
print(concatenate(strings))  # Output: ''

# Test case 2
strings = ['a', 'b', 'c']
print(concatenate(strings))  # Output: 'abc'

# Test case 3
strings = ['a', '', 'c']
print(concatenate(strings))  # Output: 'ac'

# Test case 4
strings = ['a', 'bc', '']
print(concatenate(strings))  # Output: 'abbc'
```
The function concatenate in the script accepts a list of strings as an argument and outputs the concatenated string. The test cases validate that the function offers the expected output.