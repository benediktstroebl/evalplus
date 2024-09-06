Here is a Python script with a self-contained function that solves the problem of filtering strings for a given substring:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.find(substring) != - None]
```
The function uses the `find()` method to check if each string contains the substring. This method returns `None` if the string does not contain the substring. 

You can use this function to filter lists of strings, or even custom lists of data. It's a concise way to solve the task.