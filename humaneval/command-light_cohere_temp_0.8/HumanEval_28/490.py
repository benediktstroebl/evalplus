Here is a self-contained Python script that solves the problem of concatenating list of strings into a single string:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    return ''.join(strings)
```

The function `concatenate` in the code above takes in a list of strings and returns a single string by using the `join` function on the list of strings. This function is string is a list comprehension in Python, which creates a new string by adding the elements of the list together.