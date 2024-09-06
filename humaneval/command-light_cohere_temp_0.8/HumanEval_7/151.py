Here's a self-contained Python function that filters a list of strings based on a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function takes two arguments: a list of strings (strings) and a substring (substring). The function uses the contains() method to check if each string contains the given substring, and then returns a new list containing only those strings that do contain the substring. 

The function is self-contained, meaning it can be used to filter a list of strings containing a given substring without needing to call any other functions or modules.