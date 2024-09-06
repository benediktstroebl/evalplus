Here's the provided Python function that determines the length of the longest string in a list of strings:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Returns the length of the longest string in the list.
    """
    list of strings may contain at least one character
    """
    if not strings:
        return None
    
    max_len = 0
    max_str = ""
    for string in strings:
        if len(string) > max_len:
            max_len = len(string)
            max_str = string
    return max_len

# Test case 1
print(longest(['a', 'b', 'c']))  # Output: 3

# Test case 2
print(longest(['aa', 'bb', 'ccc']))  # Output: 3

# Test case 3
print(longest(['abc', 'abcd', 'abc'))  # Output: 3
```
The code defines the longest function that takes a list of strings and returns the length of the longest string in the list. It then uses this list of strings may contain at least one character, so it checks if the list is empty and returns None in that case. It then initializes variables for the maximum length and the longest string found so far. The function iterates through each string in the list and compares its length to the current maximum length. If the length of the string is longer, the variables are updated. Finally, the function returns the longest string's length.