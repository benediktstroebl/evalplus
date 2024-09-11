```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): Input string with groups of nested parentheses.

    Returns:
        List[int]: A list of the deepest level of nesting for each group.

    Examples:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    result = []
    for group in paren_string.split():
        # Initialize a stack to keep track of opening parentheses
        stack = []
        depth = 0
        # Initialize max_depth to keep track of the maximum depth
        max_depth = 0
        for char in group:
            if char == '(':
                # If we encounter an opening parenthesis, push it onto the stack and increment depth
                stack.append(char)
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                # If we encounter a closing parenthesis, pop the corresponding opening parenthesis from the stack and decrement depth
                stack.pop()
                depth -= 1
        result.append(max_depth)
    return result

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This Python script uses a stack to keep track of the depth of nesting in each group. It iterates over the input string and for each opening parenthesis, it pushes it onto the stack and increments the current depth. When it encounters a closing parenthesis, it pops the corresponding opening parenthesis from the stack and decrements the current depth. The maximum depth encountered during this process is recorded and added to the result list.