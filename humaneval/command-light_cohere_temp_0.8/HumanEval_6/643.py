```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes in a string of nested parentheses and returns the deepest level of nesting of parentheses.
    >>> test_parse_nested_parens("(()()) ((())) () ((()))()")
    [(2, 3, 1, 3)]
    """
    # Split the string by spaces to get all groups of parentheses
    groups = s.split()
    Groups = []
    for group in groups:
        if group.startswith('('('):  # if starts with open paren
            nesting = 1
        elif group.endswith(')':  # if ends with closed paren
            nesting = len(group) - 1
        else:  # anything else, no nesting
            nesting = 0
        Groups.append(nesting)

    return Groups  # return list of nesting levels
```
This function parses a string of multiple groups of parentheses and returns the deepest level of nesting for each group. It uses a splitting on spaces to get all the groups of parentheses and uses a simple if/else statement to determine if the current group is an open or closed parenthesis.