```markdown
### Deep Nesting Levels of Parentheses

#### Problem Description
Parse a string of nested parentheses and for each group, determine the deepest level of nesting.

#### Solution

```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of nested parentheses groups separated by spaces.

    Returns:
        List[int]: A list of deepest nesting levels for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    groups = paren_string.split()
    results = []

    for group in groups:
        level = 0
        max_level = 0
        for char in group:
            if char == '(':
                level += 1
                max_level = max(max_level, level)
            elif char == ')':
                level -= 1
        results.append(max_level)

    return results

# Example usage
paren_string = '(()()) ((())) () ((())()())'
print(parse_nested_parens(paren_string))
```

#### Explanation

This script defines a function `parse_nested_parens` that takes a string of nested parentheses groups separated by spaces as input. It splits the input string into individual groups, then iterates over each group. For each group, it keeps track of the current level of nesting and the maximum level encountered so far. When it encounters a closing parenthesis, it decrements the current level. The maximum level encountered during the iteration is the deepest level of nesting for the group. The results are collected in a list, which is returned by the function.
```