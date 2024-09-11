Here is the Python script that solves the problem:
```markdown
### Parse Nested Parentheses

This script parses a string of nested parentheses and returns the maximum level of nesting for each group.

#### Code
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Parameters:
    paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of the maximum level of nesting for each group.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def max_nesting(s: str) -> int:
        """Return the maximum level of nesting for a given string of parentheses."""
        level = 0
        max_level = 0
        for char in s:
            if char == '(':
                level += 1
                max_level = max(max_level, level)
            elif char == ')':
                level -= 1
        return max_level

    return [max_nesting(group) for group in paren_string.split()]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

#### Explanation

This script defines a nested function `max_nesting` that calculates the maximum level of nesting for a given string of parentheses. It does this by iterating over the string and keeping track of the current level of nesting. If it encounters an open parenthesis, it increments the level; if it encounters a close parenthesis, it decrements the level. The maximum level of nesting is updated whenever it sees a close parenthesis.

The main function `parse_nested_parens` splits the input string into groups and applies `max_nesting` to each group. It returns a list of the maximum level of nesting for each group.

Note that this script assumes that the input string is well-formed, i.e., that every open parenthesis is eventually closed. If the input string may contain unbalanced parentheses, additional error checking would be needed.