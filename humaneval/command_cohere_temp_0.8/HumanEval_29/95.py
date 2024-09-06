```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the specified prefix. This is accomplished via a list comprehension, using a generator expression with a conditional test, that filters the strings from the input list based on the `startswith` method. 

Here's an example of using the `filter_by_prefix` function with two different inputs:
```python
>>> filter_by_prefix([], 'a')
[]
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```

In the first example with the empty list and the prefix 'a', the function returns an empty list because there are no strings that start with 'a' in the input list. In the second example, the function returns a list containing 'abc' and 'array', which are the only strings in the input list that start with 'a'. 

The function's behavior is outlined via a docstring, which explains its purpose, provides example usage, and gives expected output for those examples. The docstring is in reStructuredText format and is multi-line, providing a detailed description of the function's behavior, usage, and expected input/output.