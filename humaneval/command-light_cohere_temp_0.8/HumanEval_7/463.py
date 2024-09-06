```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```
Here's the function:
```
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```

And tests:
```
>>> filter_by_substring([], 'a')
[]
>>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
['abc', 'bacd', 'array']
```

This function is designed to filter an input list of strings, returning a new list that contains only the strings that contain the given substring. The function utilizes the value of the substring, passed as an argument to the function, and uses the `find()` method on each string in the strings list to check if it contains the substring.