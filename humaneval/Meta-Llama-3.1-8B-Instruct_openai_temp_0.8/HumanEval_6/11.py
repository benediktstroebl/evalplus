```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of deepest level of nesting of parentheses for each group.
    """
    def max_nesting(s: str) -> int:
        """
        Calculate the deepest level of nesting of parentheses in a string.

        Args:
            s (str): A string containing nested parentheses.

        Returns:
            int: The deepest level of nesting of parentheses.
        """
        nesting_level = 0
        max_level = 0
        for char in s:
            if char == '(':
                nesting_level += 1
                max_level = max(max_level, nesting_level)
            elif char == ')':
                nesting_level -= 1
        return max_level

    # Split the input string into groups and calculate the deepest level of nesting for each group
    groups = paren_string.split()
    return [max_nesting(group) for group in groups]

# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input, splits it into groups, and calculates the deepest level of nesting for each group using a helper function `max_nesting`. The `max_nesting` function iterates over the characters in the string, incrementing the nesting level when it encounters an open parenthesis and decrementing it when it encounters a close parenthesis, keeping track of the maximum level reached. The main function then applies `max_nesting` to each group in the input string and returns the results as a list.