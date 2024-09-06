```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which includes only the strings from the original list that begin with the provided prefix. As the function utilizes a list comprehension, it is concise and readable. Additionally, the function includes type hints, improving its overall clarity and aiding in potential debugging.

Here is an example of how to use the function:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```

In this example, the function is applied to a list of strings, and it returns a new list that includes only the strings that start with the `'a'` prefix. The output is a list that contains just `'abc'` and `'array'`, as these are the elements in the input list that commence with the specified prefix.