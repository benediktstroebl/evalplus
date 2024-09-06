Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_str = max(strings, key=len)
    return longest_str if len(longest_str) == max(len(s) for s in strings) else longest(
        [s for s in strings if s != longest_str]
    )
```

This script defines a function called `longest` that takes in a list of strings and returns either the longest string in the list, the first string that matches the maximum length in case of ties, or `None` if the input list is empty. The function is implemented using Python's `typing` module to ensure type safety and utilizes max with a custom key function to find the longest string in terms of length. Additionally, it includes a clever trick to handle ties in the last else statement, where it recursively calls the function with all strings that are not of the maximum length, ensuring it returns the actual longest string in case of a tie.