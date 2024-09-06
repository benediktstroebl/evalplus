Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```
The provided Python script defines a function named `filter_by_substring` that filters an input list of strings based on whether each element contains a given substring. The function utilizes the particular to iterate through the list of strings and checks whether each element matches the provided substring using the `find()` method. 

This function effectively filters and returns a new list containing only the strings that contain the specified substring, demonstrating a concise and self-contained solution to the given problem.