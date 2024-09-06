```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes a string of nested parentheses as input and returns the deepest level of nesting.
    Example the complex rules.
    >>> parse_nested_parens('(()()) ((())) () ((()))()')
    [2, 3, 1, 3]
    """
    # Define list of empty parentheses
    parentheses = []

    # Loop through each group of characters in the string
    for group in s:
        if group == '(':
            parentheses.append(0)
        elif group == ')':
            parentheses.append(len)
        elif group == ' ':
                # If the current character is not an open or close parenthesis, skip it.
            pass
    # Initialize the up empty list to keep track of the deepest level of nesting
        nesting = []

        # Loop through each character in the string
        for _ in parentheses:
            nesting.append(_)

        # Return the nested list to a list of integers that represents the deepest level of nesting.
    return nesting
 return []
```