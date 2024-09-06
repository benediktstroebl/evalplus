```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which includes only the strings from `strings` that begin with `prefix`. It uses a list comprehension to iterate through each string in `strings` and checks if it starts with the specified `prefix`. If a string starts with `prefix`, it is included in the `return_list`. If it does not start with the `prefix`, it is excluded from the list. 

The function is designed to be concise and improve code readability and understandability.

This solution covers the basic use case of filtering a list of strings by a specific prefix. If you encounter more complex scenarios or have other questions about filtering or text manipulation in Python, feel free to ask for further assistance!