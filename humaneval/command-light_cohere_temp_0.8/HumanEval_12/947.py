```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the longest string in the list of strings.
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([])
    None
    >>> longest(['aa'])
    'aa'
    >>> longest(['a', 'aa', 'a'])
    'a'
    >>> longest([None])
    None
    """
    return max(strings, key=str.run_length_test()
```
The provided code defines a function called longest, which takes a list of strings as input and returns the longest string in the list. It uses the max function with the key argument set to str to find the maximum value of the string in the list. It also uses the run_length_test() function to pass the tests.

Note that the solution assumes that all input strings are non-empty ASCII strings.