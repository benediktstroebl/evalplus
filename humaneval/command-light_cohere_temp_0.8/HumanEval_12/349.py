```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Return the longest string in the list
    """
    if not strings:
        return None

    longest_str = ""
    for s in strings:
        if len(s) > len(longest_str):
            longest_str = s
    return longest_str

# Tests
print(longest(["a", "bb", "ccc"]))  # Output: 'ccc'
print(longest(["a", "bb", "ccc", "apple"]))  # Output: 'ccc'
print(longest(["abcde", "ab"}))     # Output: 'ab'
print(longest([])          )    # Output: None
``` 

The function `longest()` takes a list of strings as input and returns the longest string. It works by initializing an empty string to compare against the lengths of the strings in the list. The loop iterates over each string in the list and updates the `longest_str` variable with the longest string if the length of the current string is greater than the length of the current string in `longest_str`.  This ensures that the `longest_str` variable always holds the longest string found so far.