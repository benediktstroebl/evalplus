```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```

This function takes a list of strings, `strings`, and a substring, `substring`, as input. It uses a list comprehension to filter the elements of the `strings` list and return a new list containing only the strings that contain the specified substring. 

Here's an example usage of the function:
```python
>>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
['abc', 'bacd', 'array']
>>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'b')
['bacd']
```

The function output is a list of strings contained in `strings` that include the character `substring`. As expected, the results of these examples are the strings that have the specified substring 'a' or 'b' respectively.