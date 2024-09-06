```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which includes only the strings from the input list that start with the input prefix. The behaviour is demonstrated in the following example:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
``` 

The function utilizes list comprehension, coupled with the `startswith` method, to efficiently filter the desired strings from the input list based on the provided prefix.