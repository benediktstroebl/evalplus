```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This Python script defines a function called `filter_by_substring` that filters a list of strings to only include those that contain a given substring. The function uses the specific type hint for the input parameter `strings`, which is a `List[str]`, and the corresponding output parameter `List[str]`, which is also a `List[str]`. It utilizes the `contains` function to iterate through the input list and return a new list containing only the strings that contain the given substring.