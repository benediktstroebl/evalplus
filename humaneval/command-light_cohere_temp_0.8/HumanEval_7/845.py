Here is a self-contained Python script that solves the problem of filtering an input list of strings for ones that contain a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains substring(string)]
```
This script defines a function called `filter_by_substring` that takes in a list of strings and a substring as input, and returns a new list containing only the strings from the input list that contain the given substring. 
The function uses the list comprehension to iterate over the input list of strings and checks if each string contains the given substring using the `contains` method.