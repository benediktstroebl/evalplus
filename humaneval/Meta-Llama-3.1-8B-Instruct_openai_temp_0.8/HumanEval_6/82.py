```markdown
## parse_nested_parens Function
### Solution to calculate the deepest level of nesting of parentheses in each group

```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting of parentheses for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    groups = paren_string.split(' ')
    result = []

    for group in groups:
        depth = 0
        max_depth = 0

        for char in group:
            if char == '(':
                depth += 1
            elif char == ')':
                max_depth = max(max_depth, depth)
                depth -= 1

        result.append(max_depth)

    return result
```

### Example Usage

```python
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script works by iterating over each group of parentheses, keeping track of the current depth and maximum depth encountered so far. When a closing parenthesis is encountered, the maximum depth is updated if the current depth is greater than the maximum depth. The maximum depth is then appended to the result list.