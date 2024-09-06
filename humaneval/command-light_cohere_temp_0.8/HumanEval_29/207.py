Here's a self-contained Python function that filters an input list of strings based on a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings and a prefix as input, and returns a new list containing only the strings from the input list that start with the given prefix. 

This function utilizes the typing module to provide type hints and improve code clarity. The function uses list comprehension to filter the strings based on whether their prefix matches the given prefix. 

Remember to use this function by simply passing in the appropriate strings list and prefix, and it will return the desired filtered list of strings.