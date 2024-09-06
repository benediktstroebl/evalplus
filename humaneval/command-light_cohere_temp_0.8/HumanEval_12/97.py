```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Returns the longest string in the list.
    Parameters: List[str]
    Returns: List[str]
    """
    return max(strings, key=len) if strings else None

# Unit tests
strings = ["hello", "world", "hello world"]
longest_res = longest(strings)
print(longest_res)  # Output: "world"
```

The code defines a function named longest, which takes a list of strings as input and returns the longest string in that list. It achieves this by utilizing the max function with the key=len argument, which returns the length of the strings in the list. The function then returns the list of strings.

The code also includes a set of strings in the unit test, and passes them to the longest function. The output of the longest function is stored in longest_res, and then printed to the console.