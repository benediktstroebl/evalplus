from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if paren_string is None:
        return []

    separate_groups = []
    group = []
    open_count = 0
    closed_count = 0
    for char in paren_string:
        if char == ')':
            open_count -= 1
        elif char == '(':
            open_count += 1
            closed_count += 1
        elif char =='':
            pass
        else:
            raise ValueError('Unrecognized character in paren_string')

        if open_count == 0:
            separate_groups.append(''.join(group))
            group = []

        if closed_count!= open_count:
            group.append(char)

    separate_groups.append(''.join(group))
    return separate_groups

