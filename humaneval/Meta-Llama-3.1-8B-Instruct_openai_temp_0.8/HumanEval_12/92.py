### Longest String Finder

Below is a self-contained Python script that implements the `longest` function according to the provided specification.

```markdown
### Code
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
        Optional[str]: The longest string or None if the list is empty
    """
    if not strings:  # Check if the list is empty
        return None
    return max(strings, key=len)  # Return the longest string

### Example Use Cases
>>> from longest_string import longest

>>> longest([])

>>> longest(['a', 'b', 'c'])
'a'

>>> longest(['a', 'bb', 'ccc'])
'ccc'
```

### Explanation
This script defines a function `longest` that takes a list of strings as input and returns the longest string. If the input list is empty, it returns `None`. To find the longest string, it uses the built-in `max` function with `key=len`, which returns the first string with the maximum length in case of a tie.

The example use cases demonstrate the function's behavior for empty lists, lists with a single string, and lists with multiple strings of the same length.