Here's a self-contained Python script with a function `filter_by_substring` that filters an input list of strings based on whether the substring is present:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings, return a new list with matching substrings.

    # Use the templates
    filter using regular expression
    return [str for str in strings if str.contains(substring)]
```
The `contains` method is used to check if a given string contains the substring. The function returns a new list containing only the strings from the input list that do contain the substring.

This script is self-contained, and it can be used to solve the problem of filtering strings based on a given substring.