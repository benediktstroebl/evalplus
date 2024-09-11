```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of the deepest level of nesting of parentheses for each group.

    Args:
        paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of the deepest level of nesting of parentheses for each group.
    """
    def find_depth(paren_group: str) -> int:
        """
        This function finds the deepest level of nesting of parentheses in a single group.

        Args:
            paren_group (str): A string of nested parentheses.

        Returns:
            int: The deepest level of nesting of parentheses in the group.
        """
        depth = 0
        max_depth = 0
        for char in paren_group:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        return max_depth

    groups = paren_string.split()
    return [find_depth(group) for group in groups]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of multiple groups of nested parentheses separated by spaces. It splits the string into individual groups, finds the deepest level of nesting of parentheses in each group using the helper function `find_depth`, and returns a list of these depths. The `find_depth` function iterates over the characters in a group, incrementing the depth when it encounters an open parenthesis and decrementing it when it encounters a close parenthesis. The maximum depth encountered is returned as the deepest level of nesting.