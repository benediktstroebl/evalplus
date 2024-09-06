Here is a Python script that contains a self-contained function that solves the problem of filtering an input list of strings based on a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes two arguments: a list of strings and a prefix. string takes advantage of the had_in_type hint provided by typing and uses the Python in operator to filter the list of strings based on the given prefix. The function then returns a list of strings that start with the given prefix.