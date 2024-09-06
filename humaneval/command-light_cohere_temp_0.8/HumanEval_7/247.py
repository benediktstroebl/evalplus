Here's the self-contained Python script with a function that filters strings for a given substring:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input and returns a new list of strings that contain the substring. The function uses the simple list comprehension to achieve this. The `contains` method is used to check if a given string contains the substring. 

I hope this script provides a complete solution to the problem.