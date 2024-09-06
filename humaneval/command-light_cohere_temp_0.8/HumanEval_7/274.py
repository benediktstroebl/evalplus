```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.find(substring) != -end]
```

This Python script defines a function called `filter_by_substring` that filters a list of strings, returning a new list containing only the strings that contain the given substring. The function utilizes the fact that the `find()` method to locate the substring within each string, and the `not:` `end` argument is used to exclude the string's end character from the search result. 
The function is designed to accept a list of strings and a single string as arguments, and it is a straightforward and self-contained solution to the problem of filtering strings based on a substring.