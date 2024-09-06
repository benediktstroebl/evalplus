Here is a self-contained Python script that defines a function called `longest()` that solves the problem you have outlined above:
```python
from typing import List

def longest(strings: List[str]):
    """
    Returns the longest string from a list of strings.
    """
    # Make sure that the input list is not empty
    if not strings:
        return None
    # Sort the list
    strings.sort()
    using the way that makes the sorting deterministic.
    # Initialize the most variable to keep track of the longest string
    longest_str = ""
    # Loop through the list
    for str in strings:
        # Update the variable with the current string
        longest_str = str if len(str) > len(longest_str) else longest_str
        # Move to the next string
        longest_str += str
    # Return the longest string
    return longest_str

# Test cases
>>> longest(['a', 'b', 'c'])
'a'
>>> longest(['a', 'bb', 'ccc'])
'ccc'
>>> longest([])
None
```

This solution uses the `typing` module to add type hints to the function parameters and return types. This makes the function more readable and can be more easily understood. It also helps a way to ensure that the function will handle only valid inputs.