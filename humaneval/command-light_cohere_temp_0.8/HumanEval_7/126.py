```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This Python function takes a list of strings and a substring as input. It then uses the efficient list comprehension to filter out only the strings that contain the given substring, producing a new list that passes the test.

The function uses the contains() method to check if a string contains the substring. This is in a functional style that is self-contained and easy to read and understand.

The function type hints the return value is a list of strings, filtered by the given substring, and the substring is passed as a parameter. 

This is a good example of a self-contained function that does not rely on other functions or modules to work properly.