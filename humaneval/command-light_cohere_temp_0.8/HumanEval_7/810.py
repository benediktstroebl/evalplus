```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

The code you've provided defines a function called **`filter_by_substring`** that filters a list of strings based on whether the substring is present within each string. It uses the type hint from Python's typing module to ensure the function signature is correct. 

The function iterates through a list of strings and the given substring, then returns a new list containing only the strings that contain the substring, effectively filtering out the strings that don't contain the substring.