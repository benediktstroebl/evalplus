```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the given substring. It uses a list comprehension, iterating over each string in `strings`, and adding those that contain `substring` to the new list.

This solution covers the given use case and aligns with the problem statement and example tests provided. Using the `typing` module, the function is annotated to indicate the expected types of inputs and the return value, improving code clarity and aiding in future maintenance and collaboration.