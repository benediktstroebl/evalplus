```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains substring]
```

# Example usage:
strings = ["abc", "bacd", "cde", "array", "abcd"]
substrings = ["a", "array"]
result = filter_by_substring(strings, substrings)
print(result)  # Output: ['abc', 'bacd', 'abcd']
```

This Python code provides a function called **filter_by_substring** that takes two arguments: a list of strings and a substring string. The function filters and returns a new list that contains only the strings from the original list that contain the given substring.