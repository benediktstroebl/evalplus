```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```

This Python code defines a function called **`filter_by_substring`** that filters a list of strings for a given substring. It uses the simple list comprehension to iterate through the input strings and check if each one contains the specified substring using the **`find`** method. The filtered list containing strings that include the substring is returned.