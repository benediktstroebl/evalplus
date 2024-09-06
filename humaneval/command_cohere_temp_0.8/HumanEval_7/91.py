```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the given substring. It uses a list comprehension, iterating over each string in `strings`, and adding those that include the substring `substring` to the new list.

The behavior is illustrated in the docstring, as well as test cases to ensure its effectiveness. In the first test case, an empty list is returned since there are no strings in the input to match the substring 'a'. In the second test case, the function returns the expected filtered list, including only those strings that contain the character 'a'.