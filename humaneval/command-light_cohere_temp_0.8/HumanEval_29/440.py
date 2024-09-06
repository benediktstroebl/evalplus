Here is a Python script that includes the function **filter_by_prefix**, which is designed to filter an input list of strings based on a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix
    >>> filter_by_prefix([abc, bcd, cde, 'array'], 'a')
    ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]
``` 

This function utilizes a list comprehension to iterate through each string in the input list. The function returns a list containing only the strings that start with the specified prefix.