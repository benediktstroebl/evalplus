Here is a Python script that includes a self-contained function to solve the problem:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

The code creates a function called **filter_by_substring** that takes in two arguments: a list of strings and a substring. The function then returns a list of all the elements from the input list that contain the given substring.