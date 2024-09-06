Here is a Python script with a self-contained function that solves the problem of filtering an input list of strings based on a given prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

The function iterates through each string in the input list and tests if the string starts with the specified prefix. It then returns a string if the condition is met, effectively filtering out the strings that do not start with the given prefix.

This approach ensures the code is clean, readable, and efficient for solving this specific problem.