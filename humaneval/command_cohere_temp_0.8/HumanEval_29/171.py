```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the input prefix. It uses a list comprehension to iterate over each string in the input `strings` and returns true if it starts with the input `prefix`.

Here is an example of how to use the function:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```

Which correctly returns the list ['abc', 'array'], since these are the only two elements in the input list that start with the 'a' prefix. 

This approach utilizes Python's str.startswith() method to efficiently filter the list of strings based on the provided prefix.  The function's type annotation, List[str], indicates that it returns a list of strings.  This is important to ensure the returned value is a list of strings and to help prevent potential type-related errors.  Overall, this function efficiently solves the problem statement.