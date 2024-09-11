```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of groups separated by spaces, each group containing multiple groups of nested parentheses.
    It returns a list where each element is the deepest level of nesting in each group.

    Args:
        paren_string (str): A string of groups separated by spaces.

    Returns:
        List[int]: A list of deepest levels of nesting in each group.
    """
    def max_depth(s: str) -> int:
        """
        Helper function to calculate the maximum depth of nesting in a string.

        Args:
            s (str): The input string.

        Returns:
            int: The maximum depth of nesting.
        """
        depth = 0
        max_depth = 0
        for char in s:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        return max_depth

    # Split the input string into groups
    groups = paren_string.split()

    # Calculate the maximum depth of nesting for each group
    depths = [max_depth(group) for group in groups]

    return depths


# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of groups separated by spaces. It calculates the maximum depth of nesting in each group by using a helper function `max_depth`. The result is a list of deepest levels of nesting in each group.