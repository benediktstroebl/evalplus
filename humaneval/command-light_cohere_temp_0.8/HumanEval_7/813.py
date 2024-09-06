```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```
This Python code defines a function called `filter_by_substring` that filters an input list of strings and returns a new list containing only the elements that contain a specific substring. The function utilizes the single element in the input list and the provided substring to make the filtering determination.