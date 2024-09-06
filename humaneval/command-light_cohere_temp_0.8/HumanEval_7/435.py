```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```
This Python code defines a function named `filter_by_substring` that filters a list of strings based on whether the substring `substring` is present in each string. 

It uses the `contains` list comprehension to iterate through each string in the input list, and the `contains` function to check if each string contains the given substring. 
This function is self-contained and does not require any additional imported modules or functions to be called.