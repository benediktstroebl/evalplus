```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This Python function filters an input list of strings, returning only the ones that start with a given prefix. The function uses the filtering using the list comprehension and the startsswith() method. The test case passes because it correctly demonstrates the function's behavior. 

Please note that the code assumes the input list is not empty, and it does not validate or perform any additional input validation.