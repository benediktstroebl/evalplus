```markdown
### Deep Nesting Levels in Nested Parentheses

#### Problem Description
The function `parse_nested_parens` takes a string of multiple groups of nested parentheses separated by spaces.
For each group, it returns the deepest level of nesting of parentheses.

#### Solution

```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
    paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of deepest level of nesting of parentheses for each group.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Split the input string into groups
    groups = paren_string.split()

    # Initialize an empty list to store the deepest nesting levels
    nesting_levels = []

    for group in groups:
        # Initialize the depth and max_depth variables
        depth, max_depth = 0, 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the depth
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            # If the character is a closing parenthesis, decrement the depth
            elif char == ')':
                depth -= 1

        # Append the max_depth to the nesting_levels list
        nesting_levels.append(max_depth)

    # Return the list of deepest nesting levels
    return nesting_levels

# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

#### Explanation
The `parse_nested_parens` function splits the input string into groups and then iterates over each group.
For each group, it keeps track of the current depth and the maximum depth encountered so far.
When it encounters an opening parenthesis, it increments the depth; when it encounters a closing parenthesis, it decrements the depth.
The function returns a list of the maximum depths for each group.