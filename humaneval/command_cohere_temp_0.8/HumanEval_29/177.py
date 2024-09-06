```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the specified prefix. It uses a list comprehension to iterate through each string in the input list and checks if it starts with the given prefix using the `startswith` function. If a string matches the condition, it is included in the resulting list.

The function's type hinting also specifies that the input list should be of type `List[str]` and the output list should also be of the same type to ensure the function behaves correctly in various scenarios.

This solution is concise and efficient, providing a straightforward way to filter strings based on a specific prefix while maintaining correct typing information.