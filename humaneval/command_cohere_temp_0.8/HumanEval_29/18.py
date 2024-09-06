```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which includes only the strings from `strings` that begin with the `prefix`. It uses a list comprehension to iterate through each string in `strings` and checks if it starts with the specified `prefix`. If a string starts with the `prefix`, it is included in the `return_list`. If it does not, it is excluded from the list. 

This approach ensures that the function is efficient, given that the comprehension is a micro-optimization that improves memory usage and increases code readability. This makes it easier to understand the function's purpose and allows developers to modify and maintain the code effortlessly.