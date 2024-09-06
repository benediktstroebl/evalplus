Here's a self-contained Python script with a function `filter_by_substring` that filters an input list of strings for those that contain a given substring:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```
This function uses the `find()` method from the string module to check if each string in the input list contains the given substring.  It uses a string's `List` and `substrings` to provide input and desired substring, respectively. The `filter_by_substring` function will return a new list that contains only the strings from the original list that contain the given substring.