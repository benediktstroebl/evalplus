Here is a Python script with a self-contained function that solves the problem of filtering an input list of strings that contain a given substring:
```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python code defines a function `filter_by_substring` that filters an input list of strings based on whether they contain a given substring. The function uses the filtering technique by iterating through the input list and checking if each string contains the specified substring using the `contains` method. The function returns a filtered list of strings that do contain the substring. 

This function is self-contained and solves the problem of filtering strings that contain a given substring, which can be very useful in various text processing tasks.