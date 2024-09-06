```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This code defines a function `filter_by_substring` that takes in a list of strings `strings` and a substring `substring` as input. It returns a new list containing only the strings from `strings` that contain the specified substring. The function uses a list comprehension, iterating over each string in `strings`, and including it in the new list if the `substring` is present in that string. 

The function's type hinting indicates that its return type is a list of strings, and the blanket `List[str]` annotation suggests that the function expects the input types to be a list of strings as well. This precludes the need for type annotations in the function arguments, but they could be included for clarity if so desired. 

This solution is concise, cleanly typed, and efficient, all while remaining readable and avoiding unexpected behaviours like mutating the original list or creating extraneous intermediate variables. 

This function can be invoked with a variety of input lists and substrings to filter and return the desired results.