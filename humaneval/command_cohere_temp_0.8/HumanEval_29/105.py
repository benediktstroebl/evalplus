```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, that contains only the strings from the input list that start with the input prefix. The function uses a list comprehension, `return [strng for strng in strings if strng.startswith(prefix)]`, to iterate over each string in the input list and check if it starts with the input prefix. If it does, the string is included in the resulting list. If it does not, the string is excluded from the resulting list. 

Here is an example of how to use this function:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```
This example uses the function to filter the list of strings ['abc', 'bcd', 'cde', 'array'] to only include strings that start with the prefix 'a', resulting in a list of ['abc', 'array']. 
The function returns the list of filtered strings. 

This implementation has a straightforward syntax, utilizing Python's typing module to enhance code clarity and the built-in `startswith` function to accomplish the filtering.