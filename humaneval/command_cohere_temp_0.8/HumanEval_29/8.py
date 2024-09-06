```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from the input list that start with the input prefix. The function uses a list comprehension, which is a concise way to create a new list by applying a condition to each element of the existing list. 

To use the function, you can call it with a list of strings and a desired prefix as shown in the provided snippet. 
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```

The expected output is a list that contains only those strings from the input list that start with the input prefix, in this case, `` ['abc', 'array'] ``.  This problem can be solved in a more concise way using Python's list comprehension, which is a powerful feature for transforming lists in a single, readable line of code.