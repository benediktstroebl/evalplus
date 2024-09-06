Here's the provided Python code with a self-contained function that filters an input list of strings based on a given substring:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```
This code defines a function called `filter_by_substring` that takes two arguments: a list of strings `strings` and a substring `substring`. The function uses the `contains` method to create a new list that contains only the elements of `strings` that contain the `substring`.