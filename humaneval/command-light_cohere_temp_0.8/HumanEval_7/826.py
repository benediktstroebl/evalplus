```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This code defines a function that takes a list of strings and a substring as input, and returns a new list containing only the strings that contain the given substring. The function uses the if statement to check if each element of the input list contains the given substring, and the resulting list contains only the elements that pass this condition.