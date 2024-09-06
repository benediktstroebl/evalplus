```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([ 'abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]
```
The function takes two parameters - a list of strings and a prefix. Using the list comprehension technique, it creates a new list that contains the strings from the input list that start with the specified prefix. 

Therefore, the code provides a solution to the given problem and passes the tests with the provided markdown code block.