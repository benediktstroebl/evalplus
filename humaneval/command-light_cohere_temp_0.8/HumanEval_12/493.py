```python
from typing import List
def longest(strings: List[str]):
    """
    Return the length of the longest string in the list.
    """
    # Iterate through
    """
    max_length = 0
    for string in strings:
        # check if the length of the string is greater than the current maximum
        if len(string) > max_length:
            max_length = len(string)
    return max_length

# Test the function with a simple example
print(longest(['a', 'b', 'c'])) 
# Output: 3

# Test with an empty list
print(longest([])) 
# Output: 0

# Test with multiple strings of the same length
print(longest(['aa', 'aa', 'aa'))) 
# Output: 3

# Test with mixed case and special characters
print(longest(['A', 'a', 'z', '!@b' ])) 
# Output: 3
```
This function takes a list of strings as input and returns the length of the longest string in the list. If the list is empty, the function returns 0.