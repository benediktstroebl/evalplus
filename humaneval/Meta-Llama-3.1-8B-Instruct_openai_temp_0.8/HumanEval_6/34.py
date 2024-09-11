```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses as input, 
    where each group of parentheses is separated by a space.
    It returns a list of the maximum nesting level of each group.

    Args:
        paren_string (str): A string of nested parentheses.

    Returns:
        List[int]: A list of maximum nesting levels.
    """
    result = []
    for group in paren_string.split():
        stack = []
        max_level = 0
        for char in group:
            if char == '(':
                stack.append(char)
                max_level = max(max_level, len(stack))
            elif char == ')':
                if stack:
                    stack.pop()
        result.append(max_level)
    return result

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script works by iterating over each group of parentheses in the input string. For each group, it uses a stack to keep track of the nesting level. When it encounters an open parenthesis, it pushes it onto the stack and updates the maximum level if necessary. When it encounters a close parenthesis, it pops the stack if it's not empty. After processing each group, it appends the maximum level to the result list.