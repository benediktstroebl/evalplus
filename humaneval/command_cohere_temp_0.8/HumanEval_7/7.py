```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This code defines a function `filter_by_substring` that takes in a list of strings `strings` and a substring `substring` as input and returns a new list containing only the strings from `strings` that contain the substring. This is achieved using a list comprehension, iterating over each string in `strings` and including it in the new list if it contains the `substring`. 

To follow best practices, the function includes type annotations, which help produce clear documentation and enable powerful type checking tools. Additionally, the function utilizes a concise and readable name, following the established convention of using lowercase with underscores for clarity and readability.