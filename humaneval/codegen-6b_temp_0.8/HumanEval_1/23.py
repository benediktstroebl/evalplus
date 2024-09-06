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

    paren_string = paren_string.replace('(', ' ').replace(')', ' ')
    paren_string = paren_string.replace(' ', '')

    balanced = [0] * len(paren_string)
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            balanced[i] += 1
        elif paren_string[i] == ')':
            balanced[i] -= 1

    curr_str = ''
    str_stack = []
    for i in range(len(balanced)):
        if balanced[i] == 0:
            curr_str += paren_string[i]
            str_stack.append(curr_str)
            curr_str = ''
        elif balanced[i] == -1:
            curr_str += paren_string[i]
            if balanced[i - 1] == 0:
                str_stack.pop()
        else:
            curr_str += paren_string[i]

    return str_stack

