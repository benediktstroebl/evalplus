Here is a Python script that contains a self-contained function `filter_by_substring`, which filters an input list of strings for ones that contain a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This function utilizes the contains() method to check if each string in the input list contains the given substring. It is expected input to be a list of strings and a substring as parameters. The function returns a list of strings that contain the substring. 

This function is self-contained and can be used to solve the given problem.