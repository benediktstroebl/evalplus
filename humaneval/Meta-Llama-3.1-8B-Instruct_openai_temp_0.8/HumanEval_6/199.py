```markdown
### Solution

```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of deepest levels of nesting for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    groups = paren_string.split()
    result = []

    for group in groups:
        levels = 0
        max_levels = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current level
            if char == '(':
                levels += 1
            # If the character is a closing parenthesis, decrement the current level
            elif char == ')':
                levels -= 1
            # Update the maximum level if the current level is greater
            max_levels = max(max_levels, levels)

        # Append the maximum level for the current group to the result list
        result.append(max_levels)

    return result

# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```
### Explanation

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of maximum levels of nesting for each group separated by spaces.

The function works by iterating over each character in each group. When it encounters an opening parenthesis, it increments the current level. When it encounters a closing parenthesis, it decrements the current level. It keeps track of the maximum level encountered so far for each group.

Finally, it returns a list of maximum levels for each group.

The example usage at the end demonstrates how to use the function with the input string '(()()) ((())) () ((())()())'.