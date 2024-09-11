```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups for nested parentheses separated by spaces.
    For each group, it outputs the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of multiple groups for nested parentheses separated by spaces.

    Returns:
        List[int]: A list of deepest levels of nesting for each group.
    """
    def max_depth(group: str) -> int:
        """Helper function to find the maximum depth of a group."""
        max_depth = 0
        current_depth = 0
        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
                if current_depth < 0:  # If we have more closing parenthesis than opening parenthesis, reset current_depth to 0
                    current_depth = 0
        return max_depth

    # Split the input string into groups and find the maximum depth of each group
    groups = paren_string.split()
    return [max_depth(group) for group in groups]

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

In this script, the `parse_nested_parens` function uses a helper function `max_depth` to calculate the maximum depth of each group. The maximum depth is updated whenever an opening or closing parenthesis is encountered. The function splits the input string into groups, calculates the maximum depth of each group, and returns a list of these depths.