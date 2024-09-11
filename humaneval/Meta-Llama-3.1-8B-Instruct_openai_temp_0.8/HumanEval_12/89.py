### Longest String in a List

Here is a Python script that solves the problem:

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
        # If the list is empty, return None
        return None

    # Use the built-in max function with a key of len to find the longest string
    return max(strings, key=len)


# Test cases
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

You can run this script using Python, and it will automatically run the test cases in the docstring to verify that the function is working correctly.