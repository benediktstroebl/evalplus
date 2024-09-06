Here is a Python script that includes the function `filter_by_prefix`, which accepts a list of strings and a prefix, and returns a new list that contains only the strings from the original list that match the given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This function implements a simple and effective solution for the given problem statement. It efficiently filters out the t is the prefix, and returns a new list containing only the strings that match the given prefix. The solution is concise, readable, and follows good coding practices.