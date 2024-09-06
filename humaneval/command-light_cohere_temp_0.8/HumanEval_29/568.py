```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This function utilizes the `startswith` method from the string module to check if each string in the input list starts with the given prefix. 

It returns a new list containing only the strings from the input list that match this condition.