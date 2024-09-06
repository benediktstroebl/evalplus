Here's a Python script with a self-contained function that solves the problem using a `stack` data structure to keep track of open parentheses for each group:
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
For each of the group, output the deepest level of nesting of parentheses.
E.g. (()()) has maximum two levels of nesting while ((())) has three.

Args:
    paren_string (str): String with multiple groups of nested parentheses separated by spaces.

Returns:
    List[int]: Indices of spaces between groups, where each element corresponds to the deepest nesting level of the respective group.
"""
    result: List[int] = []
    stack = []

    for i, char in enumerate(paren_string.replace(' ', '')):
        if char == '(':
            stack.append(i)
        elif char == ')':
            stack.pop()
            if not stack:
                result.append(i)
    return result
```
The approach is to iterate through the characters of the input string, maintaining a stack of indices of open parentheses. When we encounter a closing parenthesis, we check if the stack is empty, indicating a nested parenthesis depth of 1. If not, we pop an element from the stack (effectively counting open parentheses until we reach the matching closing parenthesis). In both cases, we append the current index to the result list, as it corresponds to the deepest nesting level for that group. The final result list contains the deepest nesting level for each group of parentheses in the input string.