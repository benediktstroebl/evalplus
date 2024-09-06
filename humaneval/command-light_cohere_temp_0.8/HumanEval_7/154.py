Here's a self-contained Python function that filters an input list of strings for a given substring:
```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function takes a list of strings and a substring as input, and returns a new list containing only the strings that contain the given substring. 

It uses the contains() method to check if each string contains the substring, and the List comprehension to filter the strings based on the condition. 

Remember that this solution assumes that the input strings are not empty and that the substring you're searching for is present in all the strings.