```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string represented multiple groups for nested parentheses 
    separated by spaces, and returns the deepest level of nesting of parentheses 
    for each group.

    Args:
        paren_string (str): A string containing multiple groups for nested parentheses.

    Returns:
        List[int]: A list of the deepest level of nesting for each group.
    """

    def count_parentheses(s: str) -> int:
        """
        Helper function to count the deepest level of nesting of parentheses.

        Args:
            s (str): A string of parentheses.

        Returns:
            int: The deepest level of nesting.
        """
        max_depth = 0
        depth = 0
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif c == ')':
                depth -= 1
                if depth < 0:
                    depth = 0
        return max_depth

    # Split the input string into groups and count the parentheses in each group
    return [count_parentheses(group) for group in paren_string.split()]

# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses and returns a list of the deepest level of nesting for each group. It uses a helper function `count_parentheses` to count the deepest level of nesting for a given string of parentheses. The main function splits the input string into groups and applies the helper function to each group.

When you run this script, it will print the deepest level of nesting for each group in the given string, as shown in the example usage.