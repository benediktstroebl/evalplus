```markdown
### Nested Parentheses Depth Calculator

#### Problem Description

This Python script calculates the maximum depth of nesting for each group of parentheses in a given string.

#### Code
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of maximum depths for each group of parentheses.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    result = []
    groups = paren_string.split()

    for group in groups:
        depth = 0
        max_depth = 0
        for char in group:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        result.append(max_depth)

    return result

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```
#### Explanation

This script splits the input string into individual groups of parentheses using `split()`. It then iterates over each group, keeping track of the current depth of nesting (`depth`) and the maximum depth encountered so far (`max_depth`). Whenever it encounters an opening parenthesis, it increments `depth` and updates `max_depth` if necessary. Whenever it encounters a closing parenthesis, it decrements `depth`. Finally, it appends the maximum depth for each group to the result list.