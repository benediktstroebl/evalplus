```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This Python function, `filter_by_substring`, is designed to filter an input list of strings and return only those that contain a given substring. 

It utilizes the `contains` typing to ensure that the input `List[str]` is passed as a sequence of strings and the `substring` parameter is a single string. 
The function uses a list comprehension to iterate through the input strings and checks if each string contains the given substring using the `contains` method. 

This function can be easily incorporated into your own code to solve the problem of filtering strings for a given substring.