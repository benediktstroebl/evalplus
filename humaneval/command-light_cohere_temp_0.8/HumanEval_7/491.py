```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```
This Python code defines a function called `filter_by_substring` that takes a list of strings and a substring as input. The function uses the unique list comprehension approach with the `find` method to filter the input list of strings. The code is well-contained and should run without any external imports.