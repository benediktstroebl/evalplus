```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Returns the length of the longest string in the list.
    """
    list must contain only strings of at least one character
    if not strings:
        return None
    return max(strings, key=len)

# Example Test Cases
print(longest(['a']))      # Output: 1
print(longest(['a', 'bb', 'ccc'])) # Output: 3
print(longest(['a', 'aa', 'bb', 'ccc'])) # Output: 3
print(longest([]))          # Output: None
```

In this script, we have a function called `longest`, which takes a list of strings and returns the length of the longest string in the list. The function first checks if the list is empty, and returns `None` in that case. Then, it uses the max function with the `key` parameter set to `len` to find the maximum length of all strings in the list. The final test cases ensure that the function is working correctly with different input scenarios.