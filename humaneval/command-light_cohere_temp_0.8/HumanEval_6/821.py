```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """ Parse a string with nested parentheses into a list of their deepest nesting level.
    Parameters:
    s: string with spaces separating each group of parentheses.
    Returns: list of integer depth of the most deeply nested grouping of parentheses.
    """Deepest level of nesting will be represented as 3 for (()) and (())(). rights, the parentheses are open.
    """Dictionaries are marked by 3 in the string.
"""
    # Dictionary to convert character string to int
    char_dict = {')': 1, '('): 2, ')': 3, '('): 4, '{': 5, '}': 6, '<': 7, '>': 8, '='': 9, '?