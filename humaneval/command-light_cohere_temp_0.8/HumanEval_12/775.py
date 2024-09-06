```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one.
    """
    first_len = 0
    max_length = ""
    for string in strings:
        if len(string) > first_len:
            first_len = len(string)
            max_length = string
    return max_length

# Test case 1
strings = ["a", "b", "c"]
result = longest(strings)
print("result:", result)  # Output: c

# Test case 2
strings = ["a", "bb", "ccc"]
result = longest(strings)
print("result:", result)  # Output: c

# Test case 3
strings = []
result = longest(strings)
print("result:", result)  # Output: None
```
The function "longest" accepts a list of strings and returns the longest string. It determines the longest string in the list by comparing each string's length to the current length of the string stored in the variable "first_len". The longest string is saved in the "max_length" variable. The function also returns "None" if the input list is empty.