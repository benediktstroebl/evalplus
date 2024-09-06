```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.string() if prefix.isalpha(prefix)]
```

This function uses a generator expression to iterate through the characters of the input string and adds any prefix that is also an English letter to the result list.