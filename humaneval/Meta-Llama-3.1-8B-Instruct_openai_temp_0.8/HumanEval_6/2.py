```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of the deepest level of nesting of parentheses for each group.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def max_depth(parens: str) -> int:
        """Calculate the maximum depth of nested parentheses in a string."""
        max_depth = 0
        current_depth = 0
        for char in parens:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
                if current_depth < 0:
                    raise ValueError("Unbalanced parentheses")
        if current_depth!= 0:
            raise ValueError("Unbalanced parentheses")
        return max_depth

    return [max_depth(group) for group in paren_string.split()]

# Test the function
paren_string = '(()()) ((())) () ((())()())'
print(parse_nested_parens(paren_string))  # Output: [2, 3, 1, 3]
```

In this script, we first define a helper function `max_depth` to calculate the maximum depth of nested parentheses in a string. We then use a list comprehension to split the input string into groups, calculate the maximum depth of each group using `max_depth`, and return the results as a list. If the input string contains unbalanced parentheses, `max_depth` raises a `ValueError`.