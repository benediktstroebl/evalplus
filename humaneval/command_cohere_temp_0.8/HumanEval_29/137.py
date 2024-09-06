```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, that contains only the strings from the input list that start with the input prefix. It uses a list comprehension to iterate over each string in `strings` and check if it starts with `prefix`, if so, it includes the string in the new list. 

Here is an example of how to use the function:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```

This would return a list that includes 'abc' and 'array' because both start with the prefix 'a'. 

The function would be unchanged if no valid strings are in the list or if the given prefix is not found in any string of the list. Thus, it will return an empty list in those cases. 
For example:
```python
>>> filter_by_prefix([], 'a')
[]
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'f')
[]
``` 

Passing an empty list or a list with no common prefix will result in an empty list as well. 
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array', 'perature'], 'a')
['array']
``` 

This would return a list containing only 'array' because it is the only string in the list that starts with the prefix 'a'. 

This function is straightforward to use and understand as it handles a common task many programmers have when dealing with strings and lists.