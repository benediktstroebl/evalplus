```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the length of the longest string in the list.
    """
    string = max(strings, key=len)
    return len(string)

# Test case
strings = ['a', 'b', 'c']
result = longest(strings)
print(result)  # Prints 3
```