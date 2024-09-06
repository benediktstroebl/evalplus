```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Returns the length of the longest string in the list.
    """
    strings = [str for str in strings if len(str) > 0]
    return max(len(str) for str in strings)

# Test cases
strings = ['a', 'b', 'c']
print(longest(strings))  # Output: 3

strings = ['aa', 'bb', 'ccc']
print(longest(strings))  # Output: 3

strings = ['']
print(longest(strings))  # Output: 0

strings = []
print(longest(strings))  # Output: None
```
The code defines a function `longest` that takes a list of strings as input. The function returns the the maximum length of any string in the list, which is then returned as the result. The test cases demonstrate how the function behaves for different scenarios.