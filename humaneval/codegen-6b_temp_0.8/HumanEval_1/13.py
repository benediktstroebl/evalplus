from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # solution 1 for this problem:
    groups = []
    for match in re.findall(r'\([^()]+?\)', paren_string):
        groups.append(match)
    return groups
    # solution 2 for this problem:
    left = 0
    max_left = 0
    max_right = 0
    for i, c in enumerate(paren_string):
        if c == '(':
            max_left = i
        elif c == ')':
            max_right = i
    assert (max_left < max_right)
    groups = []
    # groups.append(paren_string[:max_left])
    # groups.append(paren_string[max_left:max_right + 1])
    # groups.append(paren_string[max_right + 1:])
    groups.append(paren_string[:max_left])
    groups.append(paren_string[max_left + 1:max_right + 1])
    groups.append(paren_string[max_right + 1:])
    return groups

