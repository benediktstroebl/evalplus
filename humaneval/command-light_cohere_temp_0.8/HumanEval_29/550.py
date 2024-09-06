Here is a Python script that includes a self-contained function `filter_by_prefix`, which is designed to filter an input list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    >>> filter_by_prefix([abc, 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]
```
This script provides a function `filter_by_prefix`, which accepts a list of strings and a prefix, and outputs a new list that contains elements from the input list that start with the specified prefix. The function employs the process of a list comprehension, which loops through each element in the input list. 

Note: This function assumes that the input string list contains only alphabetic characters. If you example of usage is provided, the function will successfully filter the list for the specified prefix.