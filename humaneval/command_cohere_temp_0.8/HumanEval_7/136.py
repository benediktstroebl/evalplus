```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```

This function takes a list of strings, `strings`, and a substring, `substring`, as input. It uses a list comprehension to iterate through each string in the input list and checks if the `substring` is present in each string. If the `substring` is found in a string, that string is included in the resulting list and if the `substring` is not found, that string is not included in the resulting list. 

This solution passes the given tests and effectively filters the list of strings based on the provided substring. 
If you were to incorporate this function into a larger program, you could also add an additional argument, `case_sensitive=False`, to make the substring matching case-insensitive, improving the function's flexibility and adaptability to various scenarios. G