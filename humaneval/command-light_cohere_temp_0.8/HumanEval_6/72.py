```python
from typing import List
def parse_nested_parens(parenthes_str: str) -> List[int]:
    """
    This function takes in a string of nested parentheses separated by spaces.
    It returns the input is a string represented multiple groups for nested parentheses, and the corresponding level of nesting.
    Args:
    parenthes_str: The input string to be parsed

    Returns:
    List of deepest level of nesting of parentheses.
    """ return [parse(parenthes_str.split())
    if parenthes_str == ""
    return []
    return [level for level in range(4) if level <= len(parenthes_str.split()) and (level)]
```