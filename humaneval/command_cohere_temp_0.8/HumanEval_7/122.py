```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the specified substring. It uses a list comprehension, iterating over each string in `strings`, and including only those strings that contain the substring `substring`. This functionality allows you to filter strings in a list easily and return the matched strings. 

The function's type hinting also specifies that the return type is a list of strings (`List[str]`), and the type hint for the `strings` parameter is a list of strings (`List[str]`). These type annotations provide better code readability and help with catching potential type-related errors early. 

To ensure the functionality works correctly, it is recommended to verify the output against a known version of the problem statement.