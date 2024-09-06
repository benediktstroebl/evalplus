from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    max_depth = 0
    depth = 0
    group_list = []
    for char in paren_string:
        if char == '{':
            depth += 1
        elif char == '}':
            depth -= 1
        elif char == '(':
            if depth == max_depth:
                group_list.append('(')
                max_depth = max(max_depth, depth)
            elif depth > max_depth:
                group_list.append('(' * depth)
                max_depth = depth
        elif char == ')':
            if depth == 0:
                group_list.append(')')
                max_depth = max(max_depth, depth)
            elif depth < max_depth:
                group_list.append(')' * (max_depth - depth))
                max_depth = depth
    return group_list

