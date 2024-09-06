```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string in the list.
    """
    if not strings:
        return None
    
    longest_str = strings[0]
    for string in strings:
        if len(string) > len(longest_str):
            longest_str = string
    return longest_str

# Example usage
strings = ['a', 'b', 'c']
longest_result = longest(strings)
print("Longest string:", longest_result)  # Output: "c"
```