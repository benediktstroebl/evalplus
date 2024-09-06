```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```

This function takes a list of strings, `strings`, and a substring, `substring`, as input and returns a new list, `return_list`, which contains only the strings from the input list that contain the given substring. 

The function utilizes a list comprehension, enabling concise filtering of strings based on whether the `substring` is present in each string. 

To ensure proper typing, the function includes the `from typing import List` import statement and utilizes the `List[str]` type annotation, allowing the function to accept only list inputs containing strings.