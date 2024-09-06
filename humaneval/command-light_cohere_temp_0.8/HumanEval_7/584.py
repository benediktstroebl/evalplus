```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.find(substring) != -end]
``` 
This Python function, `filter_by_substring`, takes a list of strings and a substring as input and returns a new list containing only the strings from the input list that contain the given substring. The function utilizes the filter function along with the `find()` and `end` methods to achieve this behavior.