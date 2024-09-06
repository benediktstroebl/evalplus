```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, that includes only the strings from the input list that start with the input prefix. The syntax is straightforward using list comprehension with a conditional statement. It returns an empty list if the input list is empty or the input prefix is empty. 

Here is an example usage of the function for an input list `['abc', 'bcd', 'cde', 'array']` and prefix 'a':
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```
This will return a list that includes only the strings that start with the character 'a', which are 'abc' and 'array' in this case.