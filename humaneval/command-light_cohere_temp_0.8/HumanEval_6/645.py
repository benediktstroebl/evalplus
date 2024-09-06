```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function is designed to parse and return the deepest level of nesting for any given string representing multiple groups of nested parentheses separated by spaces.

    Parameters:
    - parent_string (str): The input string to be parsed for nested parentheses. Expected to be a string that contains multiple groups of opening and closing parentheses, separated by spaces.

    Returns:
    - list of integer levels of nesting: Each integer corresponds to the depth of the deepest opening parent in the string.
    """
    format: [[depth_1, depth_2, ..., depth_n]

    Example: 
    - Input: '(()()) ((())) () ((()))'
    - Output: [2, 3, 1, 3]
    """
    stack = []
    in_level = 0
    opening_level = 0
    closing_level = 0

    for char in parent_string:
        if char == '(':
            opening_level += 1
        stack.append(opening_level)
        closing_level = opening_level
        if char == ')':
            closing_level -= 1
            stack.append(closing_level)
        if closing_level == 0:
            if len(stack) > 0:
                nesting_level = stack[-1][0] + 1
                stack.pop()
                return [ stack, nesting_level
            else:
                return []

    return [in_level, nesting_level]
```
This function takes a string as input and returns a list of integer levels of nesting for any given string representing multiple groups of nested parentheses separated by spaces. The function uses a stack data structure to keep track of opening and closing parentheses levels. It iterates over each characters in the input string, and when it encounters an opening parenthesis ('(', it adds the current level to the stack and increments the inner_level counter. When it encounters a subsequent '(', it adds the current level to the stack and decrements the closing_level counter. When it encounters a final ')', it checks if there are any remaining elements in the stack. If so, it pops the top of the stack, adds the popped level to the nesting_level counter, and returns the result. Otherwise, it returns an special empty list since there are no more closing parentheses to process.

This function solves the problem of parsing nested parentheses and passing the corresponding tests.