from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if not paren_string:
        return []
    if len(paren_string) == 1:
        if paren_string in '()':
            return [paren_string]
        return []
    i = 0
    while paren_string[i] in ' ()':
        i += 1
    if i == 0:
        return []
    if paren_string[i] != '(':
        return []
    stack = []
    open_count = 0
    groups = []
    for j in range(i, len(paren_string)):
        if paren_string[j] == '(':
            open_count += 1
        elif paren_string[j] == ')':
            open_count -= 1
            if open_count == 0:
                groups.append(''.join(stack))
                stack = []
                i = j + 1
                break
        if paren_string[j] != ' ':
            stack.append(paren_string[j])
    for group in separate_paren_groups(paren_string[i:]):
        groups.append(group)
    return groups

