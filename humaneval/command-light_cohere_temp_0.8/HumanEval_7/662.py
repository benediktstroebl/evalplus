```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.find(substring) != -end]
``` 
This code defines a function called `filter_by_substring` that takes a list of strings and a substring as input and returns a new list of strings that contain the substring. The code uses a `find` function to search for the substring in each string, and then uses the `List comprehension` to filter out the strings that do not contain the substring.