```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings `strings` and a substring `substring` as input, and returns a new list containing only the strings from the input list that contain the given substring. This function solves the problem and should pass the provided tests. It uses list comprehension to iterate over the input strings and includes only those strings that contain the specified substring. 
The behaviour is specified through type hints and example tests, as shown in the original problem statement.