```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, returns the length of the longest string.

    if not strings:
        return None

    max_len = 0
    longest_str = ""

    for string in strings:
        if len(string) > max_len:
            max_len = len(string)
            longest_str = string

    return longest_str if longest_str else None

# Example usage
strings = ['a', 'b', 'c']
result = longest(strings)
print(result)  # Output: 'c'

strings = ['a', 'bb', 'ccc']
result = longest(strings)
print(result)  # Output: 'ccc'
```

This Python code defines a function `longest` that takes a list of strings as input and returns the length of the longest string in the list. The function ensures that the list is checked for emptiness before processing, and if the list is empty, it returns `None`. The function then iterates through the list of strings, maintaining the variable `max_len` and `longest_str` with the length and longest string in the list, respectively. After iterating through longest string, the function returns the longest string found. The example usage demonstrates how the testing the function with two sample lists, and the output is displayed.