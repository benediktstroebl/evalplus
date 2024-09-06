```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
The problem is efficiently solved using the contains method, which returns a boolean value if a given substring is found in a string. This allows us to quickly filter the list of strings.

This function is highly efficient and can be easily used in any project.

Note: The type List[str] was used to define the parameter strings. It represents a list of strings. The substring 'substring' is a string.