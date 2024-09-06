from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Avoid mutating the input parameter
    paren_string = paren_string.replace(' ', '')
    start = 0
    end = 0
    groups = []
    while start < len(paren_string):
        open_count = 0
        for i in range(start, len(paren_string)):
            if paren_string[i] == '(':
                open_count += 1
            elif paren_string[i] == ')':
                open_count -= 1
            if open_count == 0:
                end = i + 1
                break
        if end == 0:
            end = len(paren_string)
        groups.append(paren_string[start:end])
        start = end
    return groups

