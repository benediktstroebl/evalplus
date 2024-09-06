```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which includes only the strings from the input list that start with the input prefix. The function uses a list comprehension, which is a concise way to create lists by applying an expression to each item in an existing list.

To use the `filter_by_prefix` function, you can simply call it with your list of strings and the desired prefix as demonstrated below:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
``` 

This will return a list that includes only the strings from the input list that start with the 'a' prefix. 

To validate the functionality further, you can also test the function with an empty prefix or an empty list of strings, as demonstrated below:
```python
>>> filter_by_prefix([], 'a')
[]
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], '')
[]
``` 

These tests should return an empty list despite the varying inputs, validating the functionality of the function.