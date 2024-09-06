```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This code provides a function called `filter_by_prefix` that takes a list of strings and a prefix as input, and returns a new list that contains only the strings from the input list that start with the specified prefix. The code utilizes they `startswith` method from the `string` module to check if each string in the input list starts with the given prefix.

The `filter_by_prefix` function then iterates over the input list of strings, and adds each string to the resulting list if it starts with the specified prefix. The function utilizes the filter built-in Python to create a new list that contains only the desired strings. 

This code is a good implementation of the problem and is self-contained, as it does not require any additional imports or external functions.