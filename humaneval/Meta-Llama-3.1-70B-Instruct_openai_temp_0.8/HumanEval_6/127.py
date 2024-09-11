Here's a Python script to solve the problem:

```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.
    """
    # Split the string into groups of parentheses
    groups = paren_string.split()

    max_depths = []

    for group in groups:
        max_depth = 0
        current_depth = 0

        # Iterate over each character in the group
        for char in group:
            if char == '(':
                # If the character is an open parenthesis, increase the current depth
                current_depth += 1
                # Update the maximum depth if the current depth is greater
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                # If the character is a close parenthesis, decrease the current depth
                current_depth -= 1

        max_depths.append(max_depth)

    return max_depths


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Expected output: [2, 3, 1, 3]
```

This script defines the `parse_nested_parens` function, which first splits the input string into groups of parentheses. Then it iterates over each character in each group to calculate the maximum depth of nesting for that group. The function uses a stack-like approach (with the `current_depth` variable) to keep track of the current nesting level. The maximum depth for each group is stored in the `max_depths` list, which is returned at the end of the function.