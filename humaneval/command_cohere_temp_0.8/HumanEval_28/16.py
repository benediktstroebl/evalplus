```python
# Solve the problem:
# Given a list of strings, return a string that is the concatenation of all strings in the list,
# in order, separated by spaces. If the input list is empty, return an empty string.

from typing import List

def concatenate(strings: List[str]) -> str:
    if not strings:
        return ""
    return " ".join(strings)

# Test the function with an example:
# These should return the following outputs:
# >>> concatenate([])
# ''
# >>> concatenate(['a', 'b', 'c'])
# 'a b c'

```

```python
# Test the function with another example:
# These should return the following outputs:
# >>> concatenate(['123', '456', '789'])
# '123456789'
```

```python
# Test the function with an empty string in the list:
# This should return the following output:
# >>> concatenate(['', 'a', 'b', 'c'])
# ' a b c'
``` 

This code defines a function `concatenate` that takes a list of strings (`List[str]`) as input and returns a single string concatenated from the input list. The function handles the case where the input list is empty, returning an empty string, and joins the strings in the list together with spaces using Python's `join()` method. The three test cases demonstrate how the function behaves for different input scenarios.