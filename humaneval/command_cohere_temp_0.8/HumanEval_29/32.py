```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from the input list that start with the input prefix. The behavior of the function is explained through type annotations as follows: 
 1. The function `filter_by_prefix` takes two parameters: 
- `strings`: This is a list of strings that will be filtered to create the return list. 
- `prefix`: This is a string that is used as a prefix to filter the strings in the strings list. 
 2. The function returns a list of strings, `return_list`, which is determined as follows: anonymously iterated over each string in the `strings` list, and for each string, it checks if it starts with the `prefix`. If it does, it includes the string in the `return_list`. Otherwise, it skips the string and continues iterating without including it in the return list. 

The expected behavior of the function is explained with examples through docstrings:
```python
"""
Filter an input list of strings only for ones that start with a given prefix.

Examples:
>>> filter_by_prefix([], 'a')
[]

>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
"""
```

In the first example, the function is called with an empty list and the prefix 'a', and as expected, it returns an empty list. In the second example, the function is called with a list of strings that contain 'abc', 'bcd', 'cde', and 'array' and the prefix 'a'. It returns a list that contains 'abc' and 'array', which are the strings that start with the prefix 'a'. 

This explanation should provide enough understanding of the function's behavior and how to use it for the given problem.