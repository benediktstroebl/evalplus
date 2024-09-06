Here is a Python script with a self-contained function that solves the problem of filtering an input list of strings that contain a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
The given Python script defines a function called **filter_by_substring** that takes two arguments: a list of strings **strings** and a substring **substring**. The function returns a new list containing only the strings from the input list that contain the given substring. 

The solution uses the list comprehension to filter the strings in the list based on whether the substring is found in each string.