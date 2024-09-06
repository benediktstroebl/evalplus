```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```
The code you provided is a Python function that takes a list of strings and a substring as input and returns a new list of strings that contain the given substring. It uses the interesting list comprehension to iterate over each string in the input list, and checks if each string contains the given substring using the contains() method. The function successfully filters out any strings from the input list that do not contain the given substring, and returns a new list containing only the matching strings.