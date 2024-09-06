```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the given substring. It uses a list comprehension, iterating over each string in `strings`, and adding those that include the substring `substring` to the new list.

This solution directly returns the filtered list of strings, eliminating the need for a separate empty list return for an empty input. It also doesn't repeat the explanation in the docstring and uses a more concise and clear variable naming instead of reusing the variable name `strings` for the returned list, which improves readability.