```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string """
    return ''.join(string for string in strings)

#Test case: empty list
print(concatenate([]))  # Output: ''

#Test case: single string
print(concatenate('a'))  # Output: 'a'

#Test case: list of strings
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```
This code defines a function `concatenate` that takes a list of strings as input and returns the concatenated string. It uses a maint type hints and is self-contained, with no external dependencies. 

It then passes all the tests by outputting the correct results.