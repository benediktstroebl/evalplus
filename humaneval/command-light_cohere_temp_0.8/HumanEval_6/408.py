```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes a string containing multiple groups separated by spaces representing nested parentheses,
    and returns the deepest level of nesting for each group.

    Returns: list of integers, with length equal to the number of groups, where each integer corresponds to the depth of the deepest nesting in the group.
    """
return [int(i) for i, _ in enumerate('()'.join') if s.startswith('()') else []]
```

This function uses a list comprehension to iterate over each character in the string and checks if it starts with '(', returns an integer representing the depth of the deepest nesting for that group. The resulting list of integers will have the same length as the number of groups, and the deepest nesting level for each group will be at the end.