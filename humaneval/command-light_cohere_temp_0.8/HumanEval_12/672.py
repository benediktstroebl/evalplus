```python
from typing import List
def longest(strings: List[str]) -> str:
    # Validate input
    if not strings:
        raise ValueError("Input list cannot be empty.")

    # Initialize result
    result = None
    max_length = 0
    for string in strings:
        # Find the longest string
        if len(string) > max_length:
            max_length = len(string)
            result = string

    return result

# Test cases
strings = ["", "a", "bb", "ccc"]
longest_result = longest(strings)
print("Longest string:", longest_result)

# Another test case
empty_strings = []
empty_result = longest(empty_strings)
print("Longest string:", empty_result)
```
This script defines a function `longest` which takes a list of strings as input and returns the longest string. The function first validates the validation to ensure the list is not empty. It then iterates through strings and keeps track of the maximum length and the longest string. This process effectively finds the example of using the function on a list of strings, and another empty list.