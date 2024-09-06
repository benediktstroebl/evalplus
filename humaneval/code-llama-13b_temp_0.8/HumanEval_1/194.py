from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    all_groups = []
    groups = []
    for i, ch in enumerate(paren_string):
        if ch in '()':
            if ch == '(':
                groups.append(ch)
            elif ch == ')' and groups:
                groups.pop()
                if not groups:
                    all_groups.append(i)
    return [paren_string[l:r + 1] for l, r in zip(all_groups, all_groups[1:])]

