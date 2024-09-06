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
strings = ['a', 'bcde']
result = concatenate(strings)
print(result)  # Output: abcde
``` 
This code is a self-contained Python function named `concatenate` that takes a list of strings as input and returns a concatenated string. It uses the  `join()` method to create a new string by appending the strings in the input list to the string '`.  `'.  It is then tested with an example input of ['a', 'bcde'] and the output is printed to the console.