```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the input prefix. It uses a list comprehension to iterate over each string in `strings` and return the ones that start with the same prefix as the input `prefix` string.

Here is an example usage of the function to test its functionality:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'ar')
['array']
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'foo')
[]
```

The example usage demonstrates the correctness of the function and its ability to filter the list based on the prefix and return the desired results.