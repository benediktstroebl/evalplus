Here is a self-contained Python script that includes the function `filter_by_prefix` which solves the problem of filtering strings starting with a given prefix:

```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function is a straightforward and efficient solution to filter elements in a list that start with a given prefix. The function uses the Python list comprehension to iterate over the input list of strings and returns a new list containing only the strings that start with the specified prefix. 

This code is a great example of how to write self-contained functions that solve specific problems in a clear and readable way, using the power of Python's type hinting and list comprehension.