```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which includes only the strings from the input list that start with the input prefix. The mechanism for filtering the list applies a list comprehension loop to go through each string in `strings` and check if it starts with `prefix`. If it does, the string is added to the returning list. 

Here is an example usage of the function:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```
This example indicates that the function returns ['abc', 'array'], since these are the only two elements in the input list of strings that start with the 'a' prefix. 

This function is reusable and efficiently performs the filtering task based on the prefix criterion. It provides a clean and streamlined way to solve the problem and can be easily incorporated into various code bases.