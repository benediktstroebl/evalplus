```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This code defines a function `filter_by_substring` that takes in a list of strings (`strings`) and a substring (`substring`) as input and returns a new list of strings that contain the specified substring. It uses a list comprehension, iterating over each string in `strings`, and including those that contain the substring `substring`. 

This solution covers the given use case and satisfies the problem constraints. It is also encapsulated and provides a clear and usable function. 

The code includes type annotations, adding useful clarity, although not essential for this relatively simple function. The list comprehension could benefit from a `f-string` for readability, but this would not impact functionality.