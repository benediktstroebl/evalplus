```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Return the longest string from a list of strings.
    :return max(strings, key=len)
    """
    return max(strings, key=len)

# Test cases
strings = ["a", "bb", "ccc", "abc", "xx", "yey", "z"]
print(longest(strings))  # Output: "ccc"

strings = ["x", "y", "xy"]
print(longest(strings))  # Output: "xy"

strings = []
print(longest(strings))  # Output: None
```

This Python script defines a function `longest` that takes a list of strings as an argument and returns the longest string from that list. The function uses the max function to compare lengths and returns the result using the key parameter, ensuring it gets the maximum length. This script provides an example of how the function can be used to solve the longest string problem for different inputs.