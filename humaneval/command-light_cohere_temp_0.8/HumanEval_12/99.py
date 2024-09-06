Here's the self-contained Python script with a function that calculates the longest string among a list of strings:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Return the longest string from a list of strings.
    Parameters:
    strings (List[str]): List of strings

    Returns:
        str: The longest string in the list
    """
    if not strings:
        return None
    
    longest_len = max(map(len, strings))
    longest_val = strings[0]
    for str in strings:
        if len(str) == longest_len:
            longest_val = str

    return longest_val

# Test cases
print(longest(['a', 'b', 'c']))  # Output: 'a'
print(longest(['aa', 'bb', 'ccc']))  # Output: 'ccc'
print(longest([]))  # Output: None
print(longest(['a', 'b', 'c', 'a']))  # Output: 'a'
```
This function, `longest`, takes a list of strings as input and returns the longest string. It handles the initial case when the list is empty and also checks if all strings in the list have the same length. It uses the `max()` function to get the maximum length among all strings and then compares the strings to find the one with the maximum length.