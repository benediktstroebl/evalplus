```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of multiple groups separated by spaces.

    Returns:
        List[int]: A list of the deepest level of nesting of parentheses for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    result = []
    for group in paren_string.split():
        # Initialize a stack to keep track of the nesting level
        stack = 0
        max_level = 0
        # Initialize a counter to keep track of the number of nested pairs
        count = 0
        for char in group:
            if char == '(':
                # When we encounter an opening parenthesis, increment the stack
                stack += 1
                max_level = max(max_level, stack)
                count += 1
            elif char == ')':
                # When we encounter a closing parenthesis, decrement the stack
                stack -= 1
        # Append the maximum level of nesting to the result list
        result.append(max_level)
    return result

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```
This script defines a function `parse_nested_parens` that takes a string of groups separated by spaces as input. It splits the string into individual groups, and for each group, it iterates through the characters. When it encounters an opening parenthesis, it increments a stack; when it encounters a closing parenthesis, it decrements the stack. It keeps track of the maximum level of nesting by comparing the current stack level to the maximum level encountered so far. Finally, it appends the maximum level of nesting for each group to a result list and returns the list.