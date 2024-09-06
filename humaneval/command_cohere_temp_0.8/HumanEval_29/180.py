```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, that contains only the strings from the input list that start with the specified prefix. The function uses a list comprehension, `return [strng for strng in strings if strng.startswith(prefix)]`, to iterate over each string in the input list and check if it starts with the provided prefix using the `startswith` method. If it does, the string is included in the resulting list. If it does not, the string is excluded from the resulting list. 

To follow the problem statement, the code should ideally include type annotations and a docstring, even though it has no tests to show. 

Note: This solution assumes that the input strings are already sorted alphabetically. If the input strings are not sorted, the output may not be consistent with respect to the order of the resulting list. Therefore, it is recommended to sort the input list beforehand, if it is not already sorted, to achieve a deterministic behavior.