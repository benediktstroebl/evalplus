Here is a Python script that includes the self-contained function **longest()**:

```python
from typing import List, Optional

def longest(strings: List[str]) ->:
    """ Out of list of strings, returns the longest one, or None if empty """
    return max(strings, key=len) if strings else None

# Test case: empty list
test_empty = longest([])
# Test case: list of strings of the same length
test_simple = longest(['a', 'b', 'c'])
# Test case: list of strings of different lengths
test_diff = longest(['a', 'bb', 'ccc'])

print(test_empty)  # Output: None
print(test_simple)  # Output: 'a'
print(test_diff)   # Output: 'ccc'
``` 

This script defines a **longest()** function that returns the longest string in a list of strings, or **None** if the list is empty. The function utilizes the maximum function with the **len** function as the key, which returns the length of the longest string.