```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```
This Python function uses the find() method to check if each string in the input list contains the given substring. 
It takes two parameters: a list of strings (strings) and a substring (substring) as its arguments. 

This function effectively filters the list of strings and returns a new list that contains only the strings that include the given substring.