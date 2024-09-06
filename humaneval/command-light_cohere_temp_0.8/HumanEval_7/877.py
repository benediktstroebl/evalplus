Here is a self-contained Python script that includes the function `filter_by_substring` which solves the problem of filtering strings for a given substring:

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain the given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd']
    >>> filter_by_substring(['abc', 'bacad', 'cde'], 'bad')
    []
    """
    return [string for string in strings if substring in string]
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as arguments. The function returns a` a list of strings that contain the substring. The function can be used to filter the list of strings based on the given substring. 

This script is fully self-contained and does not require any external libraries or modules.