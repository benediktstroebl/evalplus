Here is a self-contained Python function that returns the longest string in a list of strings:
```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Out of list of strings, returns the longest one.
    """
    first string the lowest index of characters with identical length in the input strings, 
    then returns the character at that index of the first string.
    """
test_longest() function tests the function:
    """
    >>> test_longest([])
    None
    >>> test_longest(['a'])
    'a'
    >>> test_longest(['a', 'bb', 'ccc'])
    'ccc'
    """
def test_longest():
    return longest([]) == None and longest(['a']) == 'a' and longest(['a', 'bb', 'ccc']) == 'ccc'
```
The function `longest` takes a list of strings as input and returns the longest string. 

It uses the `first` string of the lowest index of characters with identical length in the input strings, then returns the character at that index of the first string.