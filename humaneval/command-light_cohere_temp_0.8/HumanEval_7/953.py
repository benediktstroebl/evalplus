```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains.find(substring)]
 using list comprehension and the 'find' method from the string module.

```
This script defines a function called `filter_by_substring` that takes a list of strings and a substring as input and returns a new list of strings that contain the substring. The function uses list comprehension to create a new list that contains only the strings from the original list that contain the substring. 

This is a self-contained solution, as it does not require any external modules or functions to be defined.