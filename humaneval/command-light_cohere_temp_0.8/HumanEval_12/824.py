```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    """
    Find the length of the longest string in the list.
    Parameters:
        strings (List[str]): List of strings
    Returns:
        Optional[str]: The longest string in the list, or None if empty
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test case
input_strings = ['a', 'b', 'c']
longest_result = longest(input_strings)
print("Longest string:", longest_result)  # Output: c
```