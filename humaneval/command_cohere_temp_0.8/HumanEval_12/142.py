Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    
    :param strings: List of strings.
    :return: Longest string.
    """
    # Check if the list is empty
    if not strings:
        return None

    # Use a loop to find the longest string
    max_length = 0
    longest_str = None
    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
            longest_str = string
        elif len(string) == max_length and longest_str is None:
            longest_str = string

    return longest_str
```

This code defines a function `longest` that takes a list of strings as input and returns either the longest string from the list or `None` if the list is empty. The code uses a loop to iterate through the list of strings, maintaining a `longest_str` variable that holds the longest string found so far and a `max_length` variable that keeps track of the maximum length encountered.

In each iteration, the code compares the length of the current string with the `max_length` and updates these values if the current string is longer. If the current string has the same length as `max_length`, and `longest_str` is still `None`, it means that we have encountered a string of the same length as the current longest string and we update `longest_str` accordingly. Finally, the code returns the value of `longest_str` at the end of the loop.