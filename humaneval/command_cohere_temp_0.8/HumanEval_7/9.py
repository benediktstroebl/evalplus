```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This code takes advantage of list comprehension to filter strings in the input list `strings` that contain the specified substring `substring`. It returns the list of filtered out strings. 

The function signature and type annotation ensure that the function takes a list of strings and a substring as arguments and returns a list of strings. 

The `typing` module is used to enforce the type annotation. 

The description also includes a test case, which the function is designed to pass. These tests can be run by calling the function with an empty list and an empty substring to return an empty list, and likewise, with a list containing the specified strings and the substring 'a', to match the expected output. 

Please let me know if you would like me to run these tests or if you would like me to make any additional enhancements to the code for more robustness, readability, or maintainability.