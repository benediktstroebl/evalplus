Here's the self-contained Python script with a function that filters an input list of strings based on a given substring:

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings for occurrences of a given substring.
    Parameters:
    strings: List of strings to filter
    substring: The substring to filter for
    Returns: List of strings that contain the substring
    """
    return [string for string in strings if string.contains(substring)]
```

This function, `filter_by_substring`, takes two parameters: a list of strings (`strings`) and a substring (`substring`). It uses the `contains.contains()` method from filter approach to check if each string in the input list contains the given substring.

This function effectively filters the input list to retain only those strings that contain the specified substring, making it self-contained and solving the given problem in one function.