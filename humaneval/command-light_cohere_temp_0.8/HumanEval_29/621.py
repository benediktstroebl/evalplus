Here is a self-contained Python script that implements the filter_by_prefix function to solve the problem:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
The function takes two parameters: strings, which is a list of strings, and prefix, which is a string to search for in the strings. It returns a string, if it starts with the given prefix, and an empty list otherwise. The code is written using Python and uses the typing module to add type hints.