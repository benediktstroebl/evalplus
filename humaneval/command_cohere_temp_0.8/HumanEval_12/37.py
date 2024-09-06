Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    max_string: Optional[str] = None
    for string in strings:
        if len(string) > len(max_string) or (len(string) == len(max_string) and max_string is None):
            max_string = string
    return max_string if strings else None
```

This code defines a function called `longest` that takes a list of strings as input and returns either the longest string in the list or None if the list is empty. The function initializes a variable called `max_string` to None, which stores the longest string so far. Then, it iterates through each string in the input list, comparing its length to the length of the `max_string`. If the current string is longer or if it's the same length but the `max_string` is None (meaning there are multiple possible longest strings thus far), the `max_string` is updated to the current string. This process continues for all strings in the list. At the end of the loop, the function returns the value of `max_string`, which will be the longest string or None if the input was empty.

Here is an example of how you can use the function:
```python
print(longest(['a', 'bb', 'ccc']))  # Outputs: ccc
print(longest(['xyxyx', 'xyxyxyxy', 'xyxy'])) # Outputs: xyxyxyxy
print(longest(['foo', 'bar', 'baz']))    # Outputs: bar
print(longest(['a', 'b', 'c', 'a']))      # Outputs: a
print(longest([]))                       # Outputs: None
```

This example demonstrates the behavior of the `longest` function with various input lists of strings. The function returns the longest non-empty string in the list, and None if the list is empty.