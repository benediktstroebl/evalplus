from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack = []
    parens = ['(', ')']
    groups = []
    i = 0
    while i < len(paren_string) and len(stack) < 2:
        if paren_string[i] == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(paren_string[i])
        i += 1
    if len(stack) != 1:
        return [paren_string]
    groups.append(''.join(stack))
    new_string = paren_string[i:]
    i = 0
    while i < len(new_string):
        if new_string[i] == '(' and new_string[i + 1] == ')':
            new_string = new_string[:i] + separate_paren_groups(new_string[i + 2:]) + new_string[i + 2:]
            i = 0
        else:
            i += 1
    groups.extend(new_string.split('('))
    groups = [x for x in groups if x != '']
    return groups

