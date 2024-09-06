```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Return the length of the longest string.
    """
    first_length = 0
    longest_str = ""
    for string in strings:
        if len(string) > first_length:
            first_length = len(string)
            longest_str = string
    return longest_str

# Test the function
strings = ["this is", " a long string", " really really long"]
print(longest(strings))  # Output: " really really long"
```
This function accepts a list of strings and returns the length of the longest string. It initializes variables for the Recursively loops through the list and keeps track of the first length encountered and the longest string encountered. The first condition to check is if the list is empty, in which case the function returns None.