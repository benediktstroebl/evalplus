```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain the substring """
    return [string for string in strings if string.contains(substring)]
```
This Python function, `filter_by_substring`, takes a list of strings and a substring as input. It uses the basic list comprehension to filter the input list and return only the strings that contain the specified substring. This function is use of the typing module to add type hints to the function signature, which is a standard practice in Python that helps improve code readability and maintainability.