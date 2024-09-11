### Longest String in a List
#### Python Solution
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.

    Args:
    strings (List[str]): A list of strings.

    Returns:
    Optional[str]: The longest string in the list, or None if the list is empty.
    """
    if not strings:
        return None
    return max(strings, key=len)

# Example usage:
if __name__ == "__main__":
    assert longest([]) == None
    assert longest(['a', 'b', 'c']) == 'a'
    assert longest(['a', 'bb', 'ccc']) == 'ccc'
    print("All assertions passed.")
```
In this script, we use the built-in `max` function with a `key` argument set to `len` to find the longest string in the list. This approach is more efficient and concise than iterating over the list to find the longest string. The `if __name__ == "__main__":` block is used to isolate the example usage and make the script executable.