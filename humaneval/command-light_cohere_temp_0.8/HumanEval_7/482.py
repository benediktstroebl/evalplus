```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
The provided Python script defines a function `filter_by_substring` that filters a list of strings based on whether the given substring is present within each string. It uses the expected syntax to create a list comprehension that iterates over the input strings and checks whether each string contains the specified substring.