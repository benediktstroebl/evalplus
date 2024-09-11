```markdown
### Parse Nested Parentheses

This script takes a string of space-separated groups of nested parentheses and returns a list of the deepest level of nesting for each group.

#### Code

```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of space-separated groups of nested parentheses.

    Returns:
        List[int]: A list of the deepest level of nesting for each group.

    Examples:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    result = []
    for group in paren_string.split():
        level = 0
        max_level = 0
        for char in group:
            if char == '(':
                level += 1
                max_level = max(max_level, level)
            elif char == ')':
                level -= 1
        result.append(max_level)
    return result

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

#### Explanation

This script works by iterating over each group of parentheses in the input string. It uses two variables, `level` and `max_level`, to keep track of the current level of nesting and the maximum level of nesting seen so far, respectively.

For each character in the group, if it's an open parenthesis, the `level` is incremented and `max_level` is updated if necessary. If it's a close parenthesis, the `level` is decremented.

Finally, the maximum level of nesting for each group is appended to the result list, which is returned at the end.