```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```

This Python code defines a function called `filter_by_substring` that filters an input list of strings and returns a new list that contains only the elements that contain a specific substring. It uses the's list comprehension with the `find()` method to check if each string contains the given substring, and then includes them in the new list. 

You can use this function with your own lists and strings to solve the problem and pass the corresponding tests.