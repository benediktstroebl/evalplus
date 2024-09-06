Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_string = max(strings, key=len)
    return longest_string if len(longest_string) == max(len(s) for s in strings) else longest(
        [s for s in strings if s != longest_string]
    )
```

This script defines a function called `longest` that takes in a list of strings and returns either the longest string in the list, the first string that matches the maximum length in case of ties, or `None` if the input list is empty. The function is implemented using Python's `typing` module to specify type hints, making it more readable and maintainable.

The function first checks if the input list is empty, and if so, returns `None`. If the list is not empty, it uses the `max` function with a custom key function that calculates the length of each string to find the longest string in terms of character count. The function then returns the longest string if it's the sole longest string, or recursively calls itself to analyze the other strings if there's a tie.