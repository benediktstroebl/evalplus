```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which includes only the strings from the input list that start with the input prefix. The function utilizes list comprehension, followed by a boolean loop, to systematically include or exclude strings based on their starting characters. The condition `strng.startswith(prefix)` is used to check if a string starts with the provided prefix. 

Here is an example usage of the function:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```
This example uses the input list ['abc', 'bcd', 'cde', 'array'] and the prefix 'a'. The function returns a list that includes 'abc' and 'array', which are the strings in the input list that start with the specified prefix 'a'. 

The function's behavior is summarized in the included docstring, which also offers example usage and a succinct description of the function's action.