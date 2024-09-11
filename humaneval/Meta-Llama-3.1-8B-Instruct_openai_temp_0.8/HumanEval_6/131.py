### Parsing Nested Parentheses
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Parse a string of nested parentheses and return a list of maximum nesting levels for each group.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of maximum nesting levels for each group.

    Examples:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def max_nesting_level(s: str) -> int:
        """
        Calculate the maximum nesting level of a single group of parentheses.

        Args:
        s (str): A string representing a group of nested parentheses.

        Returns:
        int: The maximum nesting level of the group.
        """
        nesting_level = 0
        max_level = 0
        for char in s:
            if char == '(':
                nesting_level += 1
                max_level = max(max_level, nesting_level)
            elif char == ')':
                nesting_level -= 1
                if nesting_level < 0:
                    raise ValueError("Unbalanced parentheses")
        if nesting_level!= 0:
            raise ValueError("Unbalanced parentheses")
        return max_level

    groups = paren_string.split()
    return [max_nesting_level(group) for group in groups]

# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```
This script first defines a helper function `max_nesting_level` to calculate the maximum nesting level of a single group of parentheses. It then splits the input string into groups, calculates the maximum nesting level for each group using the helper function, and returns the results as a list. The example usage at the end demonstrates how to use the `parse_nested_parens` function to parse a string of nested parentheses.