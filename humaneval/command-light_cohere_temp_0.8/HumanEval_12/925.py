```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Out of list of strings, return the longest one.
    return the string length will
    longest_length = max(len(s) for s in strings)
    longest_text = strings[0]
    
    if longest_length == len(strings[0]):
        return longest_text
    else:
        return longest_text[::-1:]  # make sure we return string as is and not list of characters
    return longest_text

# Example usage
strings = ['a', 'b', 'c']
print(longest(strings))  # Output: 'c'
```