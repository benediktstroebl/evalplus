```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the given substring. 

The function utilizes list comprehension and a generator expression, enabled by the "in" operator, to efficiently filter the desired strings from the input list. 

Would you like to know more about the problem or the coding techniques applied?