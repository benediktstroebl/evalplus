```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings `strings` and a substring `substring` as input, and returns a new list containing only the strings from the input list that contain the given substring. This solution makes use of list comprehension, and the Python typing module is used to make the function more expressive and readable. 

To test this function, you can use the following sample inputs and expected outputs:
```python
>>> filter_by_substring([], 'a')
[]
>>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
['abc', 'bacd', 'array']
>>> filter_by_substring(['abc', 'bacd', 'cde', 'arr'], 'a')
['abc', 'bacd', 'arr']
```

This script passes the given tests and solves the problem of filtering a list of strings based on a given substring.