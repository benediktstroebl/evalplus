```python
# The following code is copied verbatim from the original prompt response
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    result = ''
    for string in strings:
        result += string
    return result
``` 

This code defines a function `concatenate` that takes a list of strings as input and returns a single string as output, concatenating the input strings in the order they appear in the list. 

The function is called with the following test cases to verify its correctness:
```python
>>> concatenate([])
''
>>> concatenate(['a', 'b', 'c'])
'abc'
```

These test cases confirm the expected behavior of the function. In the first test case, an empty list is passed, resulting in an empty string. In the second test case, a list containing the strings 'a', 'b', and 'c' is passed, and the function returns 'abc', concatenating the strings as expected. 

This python script provides an effective and efficient solution to the problem, achieving a linear time complexity of O(n), where n is the number of elements in the input list.