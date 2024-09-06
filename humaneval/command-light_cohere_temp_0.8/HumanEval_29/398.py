```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This Python code defines a function called **filter_by_prefix** that filters an input list of strings based on a given prefix. The function uses the list comprehension and the **startswith** method to achieve this. 

The function takes in two parameters: a list of strings (**strings**) and a prefix string (**prefix**).