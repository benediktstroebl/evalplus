```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function takes a list of strings and a substring as input, and returns a new list containing only the strings from the input list that contain the given substring. 

To test this function, you can create a sample list of strings and a substring, and then call the filter_by_substring function with those inputs.