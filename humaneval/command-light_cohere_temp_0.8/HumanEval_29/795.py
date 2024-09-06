Here's a self-contained Python script that implements the filter_by_prefix function from the previous prompts: 

```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings and a prefix as input and returns a new list that contains only the strings that start with that prefix.