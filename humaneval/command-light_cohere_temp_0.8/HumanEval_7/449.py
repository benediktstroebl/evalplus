Here is a Python script with a self-contained function that solves the problem of filtering strings for a given substring:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```
This script defines a function called **filter_by_substring** that takes in two parameters: a list of strings **strings** and a substring **substring**. The function returns a new list containing only the strings from the input list that contain the given substring. 

Note that the code is self-contained and does not require any additional modules or functions to be called.