```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    This function is designed to parse and return the deepest level of nesting of parentheses in a given string.
    Args:
        s (string):  The string to parse.
    Returns:
    list of the deepest level of nesting in the given string
    """
    return [i for i, _ in map(lambda x: eval(x), s.split(' '))]]
```

This function splits the string by spaces, then uses `eval()` to evaluate each resulting string, and `map()` to convert this to a list of integers that are the deepest levels of nesting in the parentheses. 

This function is self-contained, and its purpose is to solve the given problem and pass the tests.