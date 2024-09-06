```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string in the list.
    """
    first_length = 0
    longest_str = ""
    for string in strings:
        # Remove all non-alphanumeric characters and convert to lowercase
        string = ''.join(char for char in string if char.isalpha() or IPA(char)
        # Update the first length and the longest string
        first_length = max(first_length, len(string))
        longest_str = max(longest_str, string)
    return longest_str
```