```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of the deepest level of nesting for each group.

    :param paren_string: A string of multiple groups of nested parentheses separated by spaces.
    :return: A list of the deepest level of nesting for each group.
    """
    groups = paren_string.split()  # Split the string into groups
    max_depths = []  # Initialize a list to store the max depths

    for group in groups:
        max_depth = 0  # Initialize the max depth for this group
        curr_depth = 0  # Initialize the current depth

        for char in group:
            if char == '(':  # If we encounter an open parenthesis, increment the current depth
                curr_depth += 1
                max_depth = max(max_depth, curr_depth)  # Update the max depth if necessary
            elif char == ')':  # If we encounter a close parenthesis, decrement the current depth
                curr_depth -= 1

        max_depths.append(max_depth)  # Add the max depth for this group to the list

    return max_depths

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # [2, 3, 1, 3]
```