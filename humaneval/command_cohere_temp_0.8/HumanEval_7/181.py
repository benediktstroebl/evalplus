```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```

This function takes a list of strings, `strings`, and a substring, `substring`, as input and returns a new list, `List[str]`, containing only the strings from the input list that contain the specified substring. It uses a list comprehension to iterate through each string in the input list and checks if the `substring` is present in each string using the `in` operator. If the substring is found, the string is included in the resulting list. If the substring is not found, the string is excluded. 
The function is designed to efficiently filter the strings and return the filtered list without modifying the original list.