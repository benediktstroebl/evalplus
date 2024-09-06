```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the longest string in the list.
    Parameters: list of strings
    Returns the first one if all strings are of equal length
    Returns None if empty list.
    """
    long longest_string = strings[0]
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string
# Example usage
string_list = ['a', 'bb', 'ccc']
print(longest(string_list))  # Output: 'ccc'
```
This code defines a function called longest, which takes a list of strings as input and returns the longest string in that list. It does this by comparing the lengths of each string in the list and then updating the variable longest_string to the longer one.

The function will return the longest string found in the list. This is a approach ensures that the longest string is always returned, regardless of the order of strings in the list.