```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This Python code defines a function called **filter_by_substring** that takes a list of strings and a substring as inputs. The function returns a filtering the list to only contain elements that contain the given substring. This is implementation uses the basic list comprehension with the **contains** method to achieve this.

The code also uses the **typing** module for better type hints and better error detection.