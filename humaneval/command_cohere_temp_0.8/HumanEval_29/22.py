```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the input prefix. This behavior is achieved through the use of a list comprehension, coupled with the `startswith` string method. 

To showcase the function, here is an example of usage: 
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```

In this example, the function is called with a list of strings and the prefix, `'a'`. The expected output is a list containing only the strings in the input that start with the given prefix, hence the function returns `['abc', 'array']`.