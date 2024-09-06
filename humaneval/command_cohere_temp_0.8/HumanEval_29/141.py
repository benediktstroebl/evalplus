```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the specified prefix. This is achieved using a list comprehension, filtering out the strings that start with the provided prefix. 

To demonstrate the functionality, we can apply the function to the following example:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```

In this example, it returns a list containing only 'abc' and 'array', filtering strings that start with the 'a' prefix. Thus, the function works correctly and efficiently for the given problem statement.