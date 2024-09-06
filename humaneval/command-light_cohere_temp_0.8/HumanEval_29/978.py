```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This Python function uses the List comprehension and the startsswith method to filter out the strings that have a specific prefix. 

The function is then tested using the Python built-in assert statement, which allows the function to make a specific assertion about the strings it returns.