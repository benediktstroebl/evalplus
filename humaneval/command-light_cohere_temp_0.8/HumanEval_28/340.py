```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    return ''.join([s.join() for s in strings])

#Test case 1: empty list
print(concatenate([]))
#Output: ''

#Test case 2: list with one item
print(concatenate(['a']))
#Output: 'a'

#Test case 3: list with more than one item
print(concatenate(['a', 'b', 'c']))
#Output: 'abc'
``` 

This code defines a function called `concatenate` that takes in a list of strings and returns a new string by concatenating the list. The output of the code block is a simple test to verify that the function works correctly.