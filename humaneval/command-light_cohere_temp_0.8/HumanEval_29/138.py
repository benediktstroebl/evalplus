Here is a Python script that defines a function, `filter_by_prefix`, which filters an input list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings by their prefix """
    return [string for string in strings if string.startswith(prefix)]
```

This function uses the Python List comprehension to filter the strings that have the given prefix. It does not require any external functions or objects and can be used to solve the problem.

Here's an example usage of the function:
```python
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))
# ['abc', 'array']
```

This will print the strings that start with 'a', which are 'abc' and 'array'.