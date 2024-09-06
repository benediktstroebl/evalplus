```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This Python function takes a list of strings and a prefix as input. It uses the filter() function with a lambda function to create a new list that only contains strings with the given prefix. The function then returns the string.