Here's the self-contained Python function:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This function uses the Python List's filter() method with the lambda function to filter a list of strings based on whether their prefix matches the given prefix. 

It returns a new filtered list that contains the strings with the given prefix.