```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This code defines a function `filter_by_substring` that takes in a list of strings (`strings`) and a substring (`substring`) as input and returns a new list of strings that contain the given substring. It uses a list comprehension to filter the input strings based on the presence of the substring and returns the filtered list. 

This solution should help you pass the tests for this specific problem. Let me know if you need any further refinements or additional assistance!