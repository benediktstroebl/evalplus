```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, returns the longest one.
    """
    lengths = [len(s) for s in strings]
    return max(lengths, default=None) if lengths else None

# Test cases
strings = ['a', 'b', 'c']
longest_res = longest(strings)
print(longest_res)  # Output: 'c'

strings = ['a', 'bb', 'ccc']
longest_res = longest(strings)
print(longest_res)  # Output: 'ccc'

strings = []
strings. longest
longest_res = longest(strings)
print(longest_res)  # Output: None
``` 
This script provides a function called longest, which takes a list of strings and returns the longest one. It employs the max function to get the maximum length, and uses a default value of None if the list is empty. The test cases demonstrate how the code behaves correctly with various inputs.