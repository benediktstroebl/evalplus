```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This Python function uses list comprehension to filter out strings that start with a specified prefix. 

You can use this function to filter any list of strings with a given prefix.