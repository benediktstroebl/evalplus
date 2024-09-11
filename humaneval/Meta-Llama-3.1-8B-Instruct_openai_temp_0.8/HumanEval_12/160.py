```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings

    Returns:
        Optional[str]: The longest string in the list, or None if the list is empty
    """
    if not strings:  # check if the list is empty
        return None

    longest_str = strings[0]  # initialize the longest string as the first one in the list
    max_len = len(longest_str)  # initialize the maximum length as the length of the first string

    for string in strings:  # iterate over the list of strings
        if len(string) > max_len:  # check if the current string is longer than the maximum length
            longest_str = string  # update the longest string
            max_len = len(string)  # update the maximum length

    return longest_str  # return the longest string

# Test cases
if __name__ == "__main__":
    print(longest([]))  # Output: None
    print(longest(['a', 'b', 'c']))  # Output: 'a'
    print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
```

Alternatively, you can use the built-in `max` function with a `key` argument to achieve the same result in a more concise way:

```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.
    """
    return max(strings, key=len) if strings else None

# Test cases
if __name__ == "__main__":
    print(longest([]))  # Output: None
    print(longest(['a', 'b', 'c']))  # Output: 'a'
    print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
```