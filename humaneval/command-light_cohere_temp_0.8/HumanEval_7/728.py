```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```

This Python function, `filter_by_substring`, takes a list of strings and a substring as input and returns a new list that contains only the elements of the input list that contain the given substring. The function uses the string.time type is in the list comprehension to achieve this.

The function utilizes the `find()` method of the string object to check if each element of the strings list contains the given substring. The `find()` method returns the number of positions from the beginning of the string where the substring is found. This way, it is used to determine if the substring is present in the string.