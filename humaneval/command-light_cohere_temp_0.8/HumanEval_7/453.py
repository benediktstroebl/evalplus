```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

The code above implements a filter_by_substring function that takes in a list of strings and a substring as input, and returns a new list containing only the strings that contain the given substring. 
This function is self-contained and effectively solves the problem of filtering strings based on a substring. 

This is a great example of a simple and reusable function that can be incorporated into larger programs and scripts.