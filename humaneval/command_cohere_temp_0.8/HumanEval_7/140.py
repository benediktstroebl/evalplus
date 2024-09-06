```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings, `strings`, and a substring, `substring`, as input. It uses a list comprehension to iterate through each string in the input list and checks if the `substring` is present in each string. If the `substring` is found in a string, that string is included in the resulting list and returned. If the `substring` is not found in any string, the resulting list will be empty. 

This solution passes the given tests and effectively filters the list of strings based on the provided substring. 
If you have any more questions or need further assistance, feel free to ask!