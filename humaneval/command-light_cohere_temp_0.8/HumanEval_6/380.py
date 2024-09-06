```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """ Parses a string with nested parentheses into a list of their depths.

    # Initialize empty list to store the deepest level of nesting
    depths = []

    # Loop through the string
    for match in s:
        if match == '(':
            depths.append(1)
        elif match == ')':
            depths.append(depths.pop()
        deepest = max(depths) - 1, None)
            depths.remove('(')
            depths.append(0)

    return depths
```

The code defines a function `parse_nested_parens` that parses a given string `s` containing nested parentheses into a list of their depths. The function uses the nested loop to iterate over each character in the string. It uses the `match` operator to check if a character is either '(' or ') and, if it is '(', appends a depth of 1 to the list of depths. The function also uses the list `depths` to store the deepest level of nesting for each pair of parentheses. The `max()` function is used to find the maximum depth of nesting among the list of depths, and the list is then cleared to remove the parentheses.