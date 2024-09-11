```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of the deepest level of nesting for each group.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    groups = paren_string.split()  # Split the string into individual groups
    max_depths = []  # Initialize a list to store the maximum depths

    for group in groups:
        max_depth = 0  # Initialize the maximum depth for this group
        current_depth = 0  # Initialize the current depth

        for char in group:
            if char == '(':  # If we encounter an open parenthesis
                current_depth += 1  # Increase the current depth
                max_depth = max(max_depth, current_depth)  # Update the maximum depth
            elif char == ')':  # If we encounter a close parenthesis
                current_depth -= 1  # Decrease the current depth

        max_depths.append(max_depth)  # Append the maximum depth to the list

    return max_depths


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```