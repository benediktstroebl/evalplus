```python
# Solve the problem:
# Given a list of strings, return the concatenation of all strings in the list, separated by spaces

from typing import List

def concatenate(strings: List[str]) -> str:
    return ' '.join(strings)
```

This Python script defines a function called `concatenate` that takes a list of strings (`List[str]`) as input and returns a single string that is the concatenation of all the strings in the input list, separated by spaces. This is accomplished by using the `join` method, which takes an iterable of strings and concatenates them with the specified separator string (in this case, a space). This function is useful for rapidly concatenating strings in a list without the need for manual concatenation using string concatenation operators (`+`).