Here's a Python script that uses a stack to solve the problem:

```markdown
### parse_nested_parens.py
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string with multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of deepest levels of nesting of parentheses for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    # Split the input string into groups
    groups = paren_string.split()

    # Initialize the stack and the result list
    stack = []
    result = []

    # Iterate over each group
    for group in groups:
        max_level = 0
        level = 0
        # Iterate over each character in the group
        for char in group:
            if char == '(':
                # Push '(' to the stack and increase the level
                stack.append('(')
                level += 1
                # Update the maximum level
                max_level = max(max_level, level)
            elif char == ')':
                # Pop '(' from the stack and decrease the level
                if stack:
                    stack.pop()
                    level -= 1
        # Append the maximum level to the result list
        result.append(max_level)

    return result


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

In this script, we use a stack to keep track of the nesting level of the parentheses. For each group, we iterate over each character and update the maximum level accordingly. Finally, we append the maximum level to the result list. The function returns the result list, which contains the deepest level of nesting of parentheses for each group.