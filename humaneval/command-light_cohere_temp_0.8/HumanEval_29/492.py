Here is a Python script that contains a self-contained function to filter an input list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This script defines a function called `filter_by_prefix` that takes in a list of strings and a prefix as input. It then returns a the filtering out the strings in the list that start with the given prefix. 

The function uses the list comprehension to iterate through the input list of strings and returns a new list containing only the strings that start with the given prefix.