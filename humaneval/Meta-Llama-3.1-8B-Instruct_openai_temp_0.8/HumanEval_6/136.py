### Python Script to Parse Nested Parentheses
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): String containing multiple groups of nested parentheses.

    Returns:
        List[int]: A list of deepest levels of nesting for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    def calculate_depth(parens: str) -> int:
        """
        Calculate the deepest level of nesting for a given string of parentheses.

        Args:
            parens (str): String of parentheses.

        Returns:
            int: Deepest level of nesting.
        """
        max_depth = 0
        current_depth = 0
        for char in parens:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        return max_depth

    # Split the input string into groups of parentheses, and calculate the depth for each group
    groups = paren_string.split()
    depths = [calculate_depth(group) for group in groups]
    return depths

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```
This script defines a function `calculate_depth` to calculate the deepest level of nesting for a given string of parentheses. It then uses this function in the `parse_nested_parens` function to split the input string into groups, calculate the depth for each group, and return the results as a list.