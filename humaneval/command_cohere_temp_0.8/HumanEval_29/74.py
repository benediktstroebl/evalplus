```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the input prefix. The function uses a list comprehension, iterating over each string in `strings`, and returning the ones that start with the `prefix`. This is achieved by using the `startswith` method. This method returns a boolean value, indicating whether the string starts with the specified prefix, and is converted to a truthy value, as part of the list comprehension. 

The function includes type annotations, using the `typing` module, to indicate that `strings` is a list of strings and `prefix` is a string. These type annotations help to provide better clarity and ensure the correct types are used when calling the function. 

To further improve the function, it would be useful to add documentation strings that provide a clear and concise description of the function's purpose, inputs, and outputs. This would make it easier for others to understand and use the function correctly.