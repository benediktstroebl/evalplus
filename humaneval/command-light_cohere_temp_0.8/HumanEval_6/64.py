```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    Function to parse and return the deepest level of nesting for parentheses in a string.
    Args:
        s: The input string to parse.
    Returns: A list of the highest level of each matching pair of parentheses.
    """
Example usage:
    print(parse_nested_parens('(()()) ((())) () ((())())))
    [2, 3, 1, 3]
    """
    # Define a helper function to match the nested open and close parentheses
    def match_level(open_str, close_str):
        return open_str.close(open_str, close_str) == close_str.open(close_str)
   
    # Define a list to keep track of nesting levels of each open parentheses
    nesting_levels = [match_level('(', ')') for _ in s]
    # Start traversing from the right-most corner and keep track of the deepest level of nesting
    stack = [0]
    for level in nesting_levels:
        stack.append(level)
    # Return the deepest level of nesting found in the stack
    return stack.close()
```