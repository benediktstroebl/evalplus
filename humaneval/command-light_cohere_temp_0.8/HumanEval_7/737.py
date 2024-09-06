```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This Python function takes a list of strings and a substring as input, and returns a new list containing only the strings from the input list that contain the given substring. 
The function utilizes the `contains` a list comprehension to iterate through each string in the input list and checks if the string contains the given substring using the `contains` method.