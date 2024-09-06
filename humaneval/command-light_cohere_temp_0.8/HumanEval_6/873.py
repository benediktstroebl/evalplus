```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    Parses a string of nested parentheses into a list of their deepest nesting levels.

    : Input is a a string of parentheses separated by spaces, e. like string may contain 0, 1, or many groups of nested parentheses.

    Returns: list of the deepest level of nesting found in the string.
    """
    a list containing the maximum nesting level of each pair of parentheses in the string.
    """
    Each level is represented as the number of parenthesis pairs in that pair, counting from the outside.
    """
In the following test, the expected output is: [2, 3, 1, 3]
    """

    # Initialize empty list to store results
    result = []

    # Iterate through each group of parentheses
    for group in s:
        # Find the deepest level of nesting in this group
        nesting_levels = 1
        for i in group:
            if i == '(':
                nesting_levels += 1
            elif i == ')':
                nesting_levels -= 1
        # Append this level of nesting to the result list
        result.append(nesting_levels)

    return result
``` 
This function uses a simple nested loop to iterate over the groups of parentheses in the string. It keeps track of the maximum level of nesting for each group and returns the deepest level of nesting found.