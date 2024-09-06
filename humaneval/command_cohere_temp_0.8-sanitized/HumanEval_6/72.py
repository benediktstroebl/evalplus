from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
For each of the group, output the deepest level of nesting of parentheses."""
    res = []
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            stack.pop()
            if not stack:
                res.append(len(stack))

    return res