```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```

This function takes a list of strings, `strings`, and a substring, `substring`, as input. It uses a list comprehension to filter the elements of the input list, returning a new list that only includes the elements that contain the given substring. 

This solution should pass the provided tests, as it correctly solves the problem of filtering a list of strings by a given substring. 
If there are additional test cases, the function should be able to handle them, provided the inputs are properly formatted.