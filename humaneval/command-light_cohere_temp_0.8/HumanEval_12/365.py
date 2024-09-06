```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """ Return the length of the longest string in the list
    """
    max_length = 0
    longest_str = ""

    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
            longest_str = string

    return longest_str
# Test the function
longest_test = [
    longest(["a", "bb", "ccc"])[
    longest(["aa", "bb", "ccc", "abc"])][0]
    longest(["abc", "abc", "abc"])[0]
print(longest_test)  # Output: 'ccc'
```