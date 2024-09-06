```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings, `strings`, and a substring, `substring`, as input. It uses a list comprehension to iterate through each string in the input list and check if the `substring` is present in each string. If the `substring` is found in a string, that string is included in the resulting list and returned. If the `substring` is not found in any string, the resulting list will be empty. 

This approach ensures that the function is efficient and avoids the need for multiple passes, making it more scalable for large input lists.