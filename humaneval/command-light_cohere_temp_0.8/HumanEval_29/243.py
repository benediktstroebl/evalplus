```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script defines a function called **`filter_by_prefix`** that filters an input list of strings based on whether their prefixes match the given **`prefix`**. The function returns a new list that contains only the strings from the input list that have a prefix matching the given prefix. 

The script uses the Python **`List`** and **`str`** types to define the input list of strings and the prefix string. It uses the method **`startswith`** to compare the given prefix with each string in the input list.