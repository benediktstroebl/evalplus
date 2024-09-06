```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python function uses the contains() method to check if each string in the input list contains the given substring. The filter_by_substring function takes in a list of strings and a substring as parameters and returns a new list that contains only the strings that contain the substring. 


This function is designed to be efficient and easy to use, and it is a good example of a self-contained function that solves a specific problem.