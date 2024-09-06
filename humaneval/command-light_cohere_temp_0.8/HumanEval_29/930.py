Here is a self-contained Python script that includes a function to filter an input list of strings based on their prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function utilizes the `startswith` method of the string class in Python to filter the strings in the list, only keeping those that start with the given prefix. 

This function can be used to filter lists of markdown code or any other text based on a given prefix.