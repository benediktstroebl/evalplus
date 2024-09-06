from typing import Dict, List, Optional
def parse_nested_parens(s: str) -> List[int]:
    """Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses."""
    results = []
    stack = []
    group_levels = {}
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            open_par = len(stack)
            while stack and stack.pop() != '(':
                pass
            close_par = len(stack)
            group_levels[open_par] = close_par
            results.append(close_par)
    
    return results