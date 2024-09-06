from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_list = []
    paren_stack = []
    last_idx = 0

    for idx, ch in enumerate(paren_string):
        if ch == "(":
            paren_stack.append(idx)
        elif ch == ")":
            start_idx = paren_stack.pop()
            paren_list.append(paren_string[start_idx:idx + 1])
        else:
            continue

    return paren_list

