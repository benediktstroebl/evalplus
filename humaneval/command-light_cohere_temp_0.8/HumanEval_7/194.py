```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```

This Python code defines a function called **`filter_by_substring`** that takes a list of strings and a substring as input. It uses the
  string method **`contains`** to check if each string contains the given substring. 

The function returns a list of strings that do contain the substring, filtered from the input list.