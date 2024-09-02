from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    chars = list(paren_string)
    stack = []
    output = []
    is_balanced = True
    while chars:
        char = chars.pop(0)
        if char not in ['(', ')']:
            continue
        if char == '(':
            stack.append(char)
        else:
            assert char == ')'
            if len(stack) == 0:
                is_balanced = False
                break
            last_open_bracket = stack.pop()
            if last_open_bracket != '(':
                is_balanced = False
                break
    while stack:
        last_open_bracket = stack.pop()
        if last_open_bracket != '(':
            is_balanced = False
            break

    if is_balanced:
        output.append(paren_string)
    if is_balanced:
        groups = separate_paren_groups(paren_string[1:-1])
        for group in groups:
            output.append(paren_string[0] + group + paren_string[-1])
    else:
        output.append(paren_string)
    return output

