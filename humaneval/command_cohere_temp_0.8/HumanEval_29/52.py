```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the input prefix. It uses a list comprehension to iterate through each string in the input `strings` list and checks if it starts with the specified `prefix`, if it does, it includes the string in the resulting list. 

Here is an example of how to use the function:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'ar')
['array']
```

The output for both test cases is a list containing only the strings from the input list that start with the given prefix.