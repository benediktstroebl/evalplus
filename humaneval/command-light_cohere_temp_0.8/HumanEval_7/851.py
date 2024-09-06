```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```

This Python code defines a function named `filter_by_substring` that filters an input list of strings based on whether each element contains a given substring. The function utilizes the basic list comprehension and the `find` method from the string objects to check if each element contains the given substring. 

Also, if you want to run this code in a Jupyter Notebook, you need to install the `typing` library first:
```
!type -m installing typing 
! pip install typing --user=all
```