```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which includes only the strings from the input list that begin with the input prefix. The function uses a list comprehension, which is a concise way to create lists in Python.

The basic syntax for the list comprehension is:
```python
return_list = [expression for item in sequence if condition]
```

This Python script solves the problem of filtering a list of strings that start with a given prefix. The function can be used like this:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'example'], 'ex')
['cde', 'example']
``` 

Which returns the list ['cde', 'example'], because these are the only strings in the input list that start with the prefix 'ex'.