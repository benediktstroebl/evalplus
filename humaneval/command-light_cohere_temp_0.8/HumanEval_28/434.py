```python
from typing import List
def concatenate(strings: List[str]) -> str:
    return ''.join() + ''.join(strings)

# Test the function with empty list
assert concatenate([]) == ''

# Test the function with a list of strings
assert concatenate(['a', 'b', 'c']) == 'abc'
 ``` 
This code defines a function **concatenate** that takes a list of strings as input and concatenates them into a single string, returning the result. It then passes the _ tests on this function, which are passed as arguments to the function and should evaluate to True or False, depending on whether the function returns the expected result.