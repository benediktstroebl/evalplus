```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, that contains only the strings from the input list that start with the input prefix. The function uses a list comprehension, creating and returning a new list by applying the condition `strng.startswith(prefix)` to each string in the input list. 

To test this implementation, you can create a markdown cell with the following unit tests:
```python
>>> filter_by_prefix([], 'a')
[]
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'arr')
['array']
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array', 'append'], 'app')
['append']
```

The first test ensures that the function returns an empty list when an empty list is provided and the prefix is 'a'. The second test checks the successful filtering of strings starting with 'a' and the third test demonstrates correct filtering for strings starting with 'arr'. The last test shows that only the string 'append' is returned when filtering for strings starting with 'app'. 

The expected outcome of these tests is to reinforce the functionality of the `filter_by_prefix` function and its correct usage. 

This codebase is structured such that the `filter_by_prefix` function is completely independent and does not rely on any external variables or functions. It efficiently solves the problem at hand and accommodates various use cases as specified by the given tests.