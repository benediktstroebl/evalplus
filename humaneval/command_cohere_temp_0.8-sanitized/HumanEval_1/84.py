from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    
    Args:
        paren_string (str): Input string containing multiple groups of parentheses
    
    Returns:
        List[str]: A list of strings, where each string represents a separate group of parentheses
    """
    if not paren_string:
        return []
    
    stack = []
    current_group = []
    result = []
    
    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = []
        elif char == ')':
            if stack:
                current_group = stack.pop()
            else:
                result.append(')')
        else:
            current_group.append(char)