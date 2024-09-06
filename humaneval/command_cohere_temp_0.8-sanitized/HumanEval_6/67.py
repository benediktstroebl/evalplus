from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
For each of the group, output the deepest level of nesting of parentheses."""
    # Initial data structure to hold results and iteratively update it
    result = [0] * len(s.split(' '))
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            stack.pop()
        elif not stack:
            result[-1] += 1
        else:
            # If the stack is not empty, the parentheses
            # are nested and we increment the result
            result[-1] += 1
    
    return result