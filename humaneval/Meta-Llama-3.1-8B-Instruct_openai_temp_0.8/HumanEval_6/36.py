```markdown
### Python Script to Parse Nested Parentheses
#### Problem Description
Input to this function is a string represented multiple groups of nested parentheses separated by spaces.
For each of the group, output the deepest level of nesting of parentheses.

#### Solution

```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    List[int]: A list of deepest levels of nesting for each group.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def calculate_depth(paren_str: str) -> int:
        """Calculate the deepest level of nesting for a given string of parentheses."""
        depth = 0
        max_depth = 0
        for char in paren_str:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        return max_depth

    groups = paren_string.split()
    output = []
    for group in groups:
        output.append(calculate_depth(group))
    return output

### Example Usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `calculate_depth` to find the deepest level of nesting for a given string of parentheses.
It then splits the input string into groups, calculates the deepest level of nesting for each group, and returns the results as a list.