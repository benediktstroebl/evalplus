```markdown
### Longest String in List

This script solves the problem of finding the longest string in a given list of strings.

#### Code

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
    if not strings:  # Check if the list is empty
        return None
    else:
        return max(strings, key=len)  # Use max function with key as length to find the longest string

# Example use cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

#### Explanation

This script uses Python's built-in `max` function to find the longest string in the list. The `max` function takes two arguments: the iterable to find the maximum from, and a key function to define the comparison criteria. In this case, the key function is `len`, which returns the length of each string. The `max` function will then return the string with the maximum length. If the input list is empty, the function returns `None`.

Note that this script uses Python's type hinting features to indicate the types of the function's arguments and return value. This can make it easier for other developers to understand how to use the function.