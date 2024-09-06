```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from the input list that start with the given prefix. The functionality is demonstrated by the following example:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```

The `filter_by_prefix` function uses a list comprehension, filtered by the `startswith` method, to generate the desired output.  This approach leverages Python's powerful list comprehension capabilities along with its support for generic typing, making the code both effective and readable. It incorporates the required function signature and demonstrates the expected behavior through a self-contained example, all while adhering to Python best practices.