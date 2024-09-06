```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

The code above defines a function called **filter_by_substring** that takes in a list of strings and a substring as arguments. The function returns a filter this list of strings that contain the given substring. The function uses the string's **contains** method to check if each string contains the given substring.