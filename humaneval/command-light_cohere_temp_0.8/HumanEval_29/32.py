```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This code snippet presents a function called **`filter_by_prefix`** designed to filter an input list of strings based on a given prefix. It employs the filtered list comprehension, allowing the function to accept a list of strings and a prefix as arguments. 

This function efficiently outputs a new list containing only the strings from the input list that start with the provided prefix. 

I can also use this function to test it. For example:
```python
strings = ['abc', 'bcd', 'cde', 'array', 'xx', 'yyy']
prefix = 'a'
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['abc', 'array']
```