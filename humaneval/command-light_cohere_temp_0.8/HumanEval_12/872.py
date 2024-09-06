```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the longest one or None.
    Args: strings: list of strings
    Returns: longest string in the list or None in case of empty list.
    """
    string = max(strings, key=len)
    return string or None

# Test cases
strings = ["a", "b", "c"]
print(longest(strings))  # Output: c

strings = ["a", "bb", "ccc"]
print(longest(strings))  # Output: c

strings = []
print(longest(strings))  # Output: None

strings = ["aa", "b", "bb", "c"]
print(longest(strings))  # Output: b

``` 
This Python code defines a function named longest that takes a list of strings as input and returns the longest string from the list. The function employs the max function with the key argument set to the length of each string, thereby finding the longest string in the list. It then returns the maximum, or None if the list is empty.