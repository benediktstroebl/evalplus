Here is a self-contained Python script that defines and runs a function that solves the problem you have outlined:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Find the length of the longest string.
    """
    biggest_length = 0
    longest_str = ""
    for string in strings:
        if len(string) > biggest_length:
            biggest_length = len(string)
            longest_str = string
    return longest_str

# Example usage
strings = ["a", "b", "c"]
result = longest(strings)
print(result)
```

This script provides a function `longest` that takes a list of strings as input and returns the length of the longest string. The example usage demonstrates how to use the function with a sample input list and prints the result.