```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings, `strings`, and a substring, `substring`, as input and returns a new list, `L`, of strings from `strings` that contain the substring. It uses a list comprehension to iterate through each string in `strings` and checks if the `substring` is present in each string, if it is, the string is included in the new list. 

Here is an example of how to use the function:
```python
>>> filter_by_substring(
    ["abc", "bacd", "cde", "array"], 
    "a"
)
['abc', 'bacd', 'array']
```
This will return a list of all strings in the input that contain the character 'a'.