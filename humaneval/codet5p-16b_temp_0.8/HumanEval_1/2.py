from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    group_stack = []
    result_strings = []
    for c in paren_string:
        if c == '(':
            group_stack.append(c)
        elif c == ')':
            group_stack.pop()
            if len(group_stack) == 0:
                result_strings.append(paren_string[:result_strings.__len__()])
                paren_string = paren_string[result_strings.__len__():]

    return result_strings
