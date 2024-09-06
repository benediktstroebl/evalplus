```python
from typing import List
def concatenate(strings: List[str]): 
    """ Concatenate list of strings into a single string """
    return ''.join(*strings)

# Test
strings = ['a', 'b', 'c']
result = concatenate(strings)
print(result)  # Output: 'abc'
``` 
This code defines a function **concatenate** that takes a list of strings as input and concatenates them into a single string. It uses the general list unpacking to convert the list of strings into individual strings and then concatenates them with the **' ' character to form the result.