Here is a Python script that solves the problem:

```markdown
### Parse Nested Parentheses

This script takes a string of groups of nested parentheses as input, 
and returns the deepest level of nesting for each group.

```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
    paren_string (str): A string of groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of the deepest level of nesting for each group.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def max_nesting(s: str) -> int:
        """ Helper function to calculate the maximum nesting level of a string. """
        max_level = 0
        current_level = 0
        for char in s:
            if char == '(':
                current_level += 1
                max_level = max(max_level, current_level)
            elif char == ')':
                current_level -= 1
        return max_level

    # Split the input string by spaces and calculate the maximum nesting for each group
    return [max_nesting(group) for group in paren_string.split()]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

### Explanation

*   We use a helper function `max_nesting` to calculate the maximum nesting level of a single string of parentheses.
*   We split the input string by spaces and for each group, we call the `max_nesting` function to get the maximum nesting level.
*   We return a list of the maximum nesting levels for all groups.