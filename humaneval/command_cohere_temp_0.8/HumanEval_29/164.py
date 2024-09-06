```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the specified prefix. It uses a list comprehension to iterate over each string in the input `strings`, and checks if the string starts with the provided `prefix` using the `startswith` method. If it does, the string is included in the resulting list. If it doesn't, the string is excluded from the list. 

The function's behavior is demonstrated in its docstring via two example tests. These tests are both case diagrams that showcase the function's behavior for different input scenarios. The first case diagram is defined using a list of strings (`strings`) and a prefix (`prefix`). It shows how the function correctly returns an empty list `[]` when an empty `strings` list is given, and it shows that no strings in the list start with the prefix. The second case diagram is defined in the same way, but it shows the function correctly returning a list (`['abc', 'array']`) with only the strings from the `strings` list that start with the prefix when the `strings` list contains strings like 'abc', 'bcd', 'cde', and 'array'. 

Overall, the function is a self-contained and straightforward solution to the problem, and its docstring provides intuitive testing cases to verify its behavior.