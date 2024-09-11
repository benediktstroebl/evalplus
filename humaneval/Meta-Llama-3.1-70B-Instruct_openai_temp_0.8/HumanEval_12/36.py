### Longest String in a List

Here's a Python function that solves the problem. This function iterates over the list of strings, keeping track of the longest string encountered so far. If the list is empty, it returns `None`.

```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    """
    if not strings:  # Check if the list is empty
        return None

    longest_str = strings[0]  # Initialize the longest string as the first string in the list
    for string in strings[1:]:  # Iterate over the rest of the list
        if len(string) > len(longest_str):  # Check if the current string is longer than the longest string
            longest_str = string

    return longest_str


# Example usage
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
print(longest(['apple', 'banana', 'cherry']))  # 'banana'
```

Alternatively, you can use the built-in `max` function with a key function to find the longest string in a more concise way:

```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    """
    return max(strings, key=len, default=None)


# Example usage
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
print(longest(['apple', 'banana', 'cherry']))  # 'banana'
```