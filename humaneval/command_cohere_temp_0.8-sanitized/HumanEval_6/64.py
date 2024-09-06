from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
For each of the group, output the deepest level of nesting of parentheses."""
    result: List[int] = []
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(len(stack))
        elif char == ')':
            if not stack:
                result.append(0)
            else:
                stack.pop()
                result.append(len(stack))
    
    return result