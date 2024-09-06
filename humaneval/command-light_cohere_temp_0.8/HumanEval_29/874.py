```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This Python code defines a function called **filter_by_prefix** that filters an input list of strings based on whether their prefixes match a given prefix. 

The function utilizes the **List comprehension** with a filtering condition to achieve this.