```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    """
    if not strings:  # Check if the input list is empty
        return None

    max_length = max(len(s) for s in strings)  # Find the length of the longest string
    longest_strings = [s for s in strings if len(s) == max_length]  # Find all strings with the max length

    return longest_strings[0]  # Return the first one


# Test cases
assert longest([]) is None
assert longest(['a', 'b', 'c']) == 'a'
assert longest(['a', 'bb', 'ccc']) == 'ccc'
```