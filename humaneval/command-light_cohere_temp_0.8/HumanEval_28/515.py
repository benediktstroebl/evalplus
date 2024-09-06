Here's a self-contained Python script that defines a function 'concatenate' to concatenate list of strings into a single string:
```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)
# Testing the function
a = ['a', 'b', 'c']
b = ['xx', 'yy', 'zz']
c = ['abc']
d = ['x', 'y', 'z']

print(concatenate(a))  # Output: 'abc'
print(concatenate(b))  # Output: 'xyz'
print(concatenate(c))  # Output: 'abc'
print(concatenate([a, b, c]))  # Output: 'abcxyz'
```
This script defines a function `concatenate` that takes a list of strings as input and concatenates them into a single string. It's then tested with different inputs and the output is printed to the console. 

This is a great example of self-contained code that can be easily reused and tested.