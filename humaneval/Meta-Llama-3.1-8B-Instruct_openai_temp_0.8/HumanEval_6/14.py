```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the deepest level of nesting of parentheses 
    for each group in the input string.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses 
                        separated by spaces.

    Returns:
    List[int]: A list of integers representing the deepest level of nesting for each group.
    """
    def max_nesting(s: str) -> int:
        """Helper function to calculate the deepest level of nesting for a single group."""
        stack = 0
        nesting = 0
        for char in s:
            if char == '(':
                stack += 1
                nesting = max(nesting, stack)
            elif char == ')':
                if stack > 0:
                    stack -= 1
            else:
                raise ValueError("Input string should only contain parentheses.")
        if stack!= 0:
            raise ValueError("Unbalanced parentheses in the input string.")
        return nesting

    # Split the input string into groups and calculate the nesting level for each group
    groups = paren_string.split()
    result = [max_nesting(group) for group in groups]
    return result

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input, splits it into groups, and calculates the deepest level of nesting for each group using a helper function `max_nesting`. The result is a list of integers representing the deepest level of nesting for each group. The example usage demonstrates how to call the function with the provided input string.