Here is a self-contained Python script that defines a function filter_by_prefix that solves the problem you've described, which filters an input list of strings based on a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix """
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings and a prefix as input, and returns a new list that contains only the strings from the input list that start with the specified prefix. 

Please note that the comments are provided to better explain the purpose of each function or code.