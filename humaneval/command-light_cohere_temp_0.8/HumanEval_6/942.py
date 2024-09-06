Here is a self-contained Python script that solves the problem you described:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes in a string of nested parentheses separated by spaces and returns the deepest level of nesting for each group.

    Parameters:
    s (str): A string containing multiple groups of parentheses separated by spaces.

    Returns:
    A list of integers representing the deepest level of nesting for each group.

    """
    return [map(lambda x: (x == '()' and len(x.group()) > 1) orgroups(s), lambda g: [len(g), g]))
```
Do you need help with anything else?