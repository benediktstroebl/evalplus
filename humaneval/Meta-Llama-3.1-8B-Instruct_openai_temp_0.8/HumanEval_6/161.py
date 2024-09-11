```markdown
### Nested Parentheses Parser
#### A Python Script to Calculate the Deepest Level of Nesting in Nested Parentheses

```python
from typing import List

def calculate_depth(s: str) -> int:
    """Calculate the depth of the deepest nesting in the string `s`"""
    depth = 0
    max_depth = 0
    for char in s:
        if char == '(':
            depth += 1
            max_depth = max(max_depth, depth)
        elif char == ')':
            if depth > 0:
                depth -= 1
    return max_depth


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting in each group.
    """
    # Split the input string into groups
    groups = paren_string.split()

    # Initialize an empty list to store the results
    results = []

    # Iterate over each group
    for group in groups:
        # Calculate the depth of the deepest nesting in the current group
        depth = calculate_depth(group)
        # Append the result to the list
        results.append(depth)

    # Return the list of results
    return results


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines two functions: `calculate_depth` and `parse_nested_parens`. The `calculate_depth` function calculates the depth of the deepest nesting in a given string of parentheses. The `parse_nested_parens` function splits the input string into groups, calculates the depth of the deepest nesting in each group using `calculate_depth`, and returns a list of these depths.