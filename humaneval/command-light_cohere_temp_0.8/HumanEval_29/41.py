```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings and a prefix as input and returns a new list containing only the strings that start with the given prefix. The function utilizes the string slicing and list comprehension to achieve this. The example test cases are provided to demonstrate the functionality of the function, and they correctly return the expected results.