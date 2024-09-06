```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]

 # Example code here
```

This Python script defines a function `filter_by_substring` that filters an input list of strings, returning a new list containing only those strings that contain the specified substring. 

This is a self-contained solution, and it can be used to filter lists of strings in Markdown code blocks, such as in a documentation file.