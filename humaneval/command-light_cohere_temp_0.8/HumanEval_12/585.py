```python
from typing import List
def longest(strings: List[str]):
    """
    Return the longest string from a list of strings.
    """
    return max(strings, key=len)

# Test case 1
strings = ["a", "b", "c"]
result = longest(strings)
print(result)  # Output: c

# Test case 2
strings = ["a", "bb", "ccc"]
result = longest(strings)
print(result)  # Output: ccc

# Test case 3
strings = []
result = longest(strings)
print(result)  # Output: None
```

This Python script defines a function `longest` that takes a list of strings as input and returns the longest string from the list. The function utilizes the string `max` function with a key parameter set to the string length, which returns the longest string. The script also passes three test cases: case 1, in which the input list is `[a, b, c]` and the output is `c`, which is the longest string; case 2, in which the input list is `[a, bb, ccc]` and the output is `ccc`, which is the longest string; and case 3, in which the input list is empty, and the output is `None` since there is no string in the list.