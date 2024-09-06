```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

The code employs the **startswith** method from the string module to filter the strings by their prefixes. The function returns a list containing the strings from the input list that start with the specified prefix.