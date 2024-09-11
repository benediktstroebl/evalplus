### Solution

```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
    paren_string (str): String containing groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of deepest level of nesting for each group.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    groups = paren_string.split()
    levels = []

    for group in groups:
        level = 0
        max_level = 0

        for char in group:
            if char == '(':
                level += 1
                max_level = max(max_level, level)
            elif char == ')':
                level -= 1

        levels.append(max_level)

    return levels

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

### Explanation

This Python script defines a function `parse_nested_parens` that takes a string of nested parentheses as input, splits it into individual groups, and calculates the deepest level of nesting for each group.

Here's a step-by-step breakdown:

1.  The function splits the input string into individual groups using the `split` method.
2.  It iterates over each group, initializing two variables: `level` to keep track of the current nesting level and `max_level` to store the maximum level encountered so far.
3.  For each character in the group, it increments `level` when encountering an opening parenthesis `(` and decrements it when encountering a closing parenthesis `)`.
4.  It updates `max_level` whenever it encounters a deeper level than the current maximum.
5.  Finally, it appends the maximum level encountered in each group to the `levels` list.
6.  The function returns the `levels` list containing the deepest level of nesting for each group.

You can test the function with the provided example to see the output: `[2, 3, 1, 3]`.