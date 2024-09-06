```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from `strings` that start with the `prefix`. It uses a list comprehension, which is a powerful Python idiom for creating new lists by performing a transformation on each item in the existing list. 

To use the function, you can simply call it with a list of strings and a desired prefix as shown below:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```

This will return a list that only contains the strings 'abc' and 'array', which are the only elements in the provided list that start with the prefix 'a'. 

This approach utilizes the `startswith` method, which is specifically designed to efficiently identify substrings at the beginning of a string, achieving the desired behavior for the provided problem.