```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the length of the longest string in the list.
    Args:
        strings (List[str]): List of strings.
    Returns: the length of the longest string.
    Returns: None if the list is empty.
    """
   
    below shows the test cases
    >>> longest(['a', 'b', 'c'])
    4
    >>> longest(['a', 'bb', 'ccc'])
    5
    >>> longest([''])
    """
```
In this script, we have a function called "longest" that takes a list of strings as input and returns the length of the longest string. The function uses the test cases, such as checking if the list is empty or has only one element, or if the list has more than one element of the same length. The function then returns None in case of the latter two test cases.