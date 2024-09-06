Below is a Python script that contains a self-contained function that filters strings for a given substring:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function employs the contains() method to determine whether each string from the input list contains the given substring. 

Would you like any other code related or any further assistance with this problem?