from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    groups = []
    i = 0
    while i < len(paren_string):
        open_count = 0
        close_count = 0
        for char in paren_string:
            if char == '(':
                open_count += 1
            if char == ')':
                close_count += 1
            if open_count == close_count:
                group = paren_string[i:i + (open_count + close_count)]
                i += open_count + close_count
                groups.append(group)
                break
        i += 1
    return groups

