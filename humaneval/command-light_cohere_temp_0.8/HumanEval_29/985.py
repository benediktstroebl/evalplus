Here is a self-contained Python script that defines a function `filter_by_prefix` solving the problem:

```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function filters a list of strings and returns a new list that contains only the strings that start with the given prefix. It uses the example of using the following input:

```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```

This code is self-contained, and it does not require any external modules or functions.  It's testing, the `filter_by_prefix` function will return the expected output, which is a list of strings that start with the specified prefix.