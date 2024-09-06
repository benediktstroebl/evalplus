```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which includes only the strings from the input list that start with the input prefix.

The function utilizes list comprehension, accompanied by an implied loop, to iterate through each element in the input list. It checks if each element, represented as a string, starts with the specified prefix. The `startswith` method is used for this check. If the condition is met, the string is included in the `return_list`.

Note that the function includes type annotations, indicating that the input argument `strings` is a list of strings and the `prefix` is a string. These annotations are beneficial for code clarity and improved IDE support.