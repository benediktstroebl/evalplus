from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    """Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those groups into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string."""
    result: List[str] = []
    stack: List[str] = []
    for char in paren_string:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if not stack or stack.pop() != '(':
                result.append('')
            elif not stack:
                result.append('')
            else:
                result.append('')
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            result[-1] += char

    # Add remaining open parentheses
    while stack and stack[-1] == '(':
        result.append('')
        stack.pop()
    
    return result