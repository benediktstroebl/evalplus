```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from the input list that start with the given prefix. The behaviour of the function is defined by the following:
- If `strings` is an empty list or the prefix is an empty string, the function returns an empty list.
- If a string in the list starts with the prefix, it is included in the returned list. 

The function uses a list comprehension, creates a new list, and checks if each string in the input list starts with the given prefix. This behaviour is expressed in the included tests:
```python
>>> filter_by_prefix([], 'a')
[]
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'ar')
['array']
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array', 'abc123'], 'abc')
['abc', 'abc123']
``` 

Given the behaviour and the tests, this code snippet is a solution to the problem statement. 
It's important to note that this code assumes that the prefix is a substring of the strings in the list, which might not always be the case in more complex scenarios. If more sophisticated matching is required (e.g., case-insensitive, wildcard characters), further modifications would be necessary.