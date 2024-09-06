```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

The function returns a new list containing only the strings from the input list that start with the specified prefix. 

Please note that the code is missing an indentation and could be better organized for readability, by using docstrings and multiple lines for readability.