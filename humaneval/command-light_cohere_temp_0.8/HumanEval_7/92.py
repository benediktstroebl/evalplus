```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
This Python code defines a function `filter_by_substring` that filters a list of strings based on whether the substring is present in each string. 

This function leverages the `find()` method of strings in Python, which returns the first occurrence of a substring match in a string. 

This is a self-contained function that demonstrates how to solve a specific problem using the `find()` method. 

This function can be used to filter lists of strings for specific substring matches, which is a common task in many programming languages and applications.