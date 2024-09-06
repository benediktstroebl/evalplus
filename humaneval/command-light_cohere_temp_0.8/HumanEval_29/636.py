```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This Python function filters a list of strings based on whether they start with a specific prefix. 

It uses a simple list comprehension with a filtering condition to achieve this. 

The function is designed to be easy to read and understand, and it is self-contained, meaning it does not rely on any other functions or modules to work.