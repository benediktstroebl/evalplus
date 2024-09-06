```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function takes in a string with multiple groups of nested parentheses separated by spaces.
    It returns the Nesting levels of all parentheses.
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Initialize empty list to store results
    result = []

    # Iterate through each group of parentheses
    for group in parent_string.group():
        # Split group into list of inners
        result.append(parse_nested_parens(inners))
    return result
```