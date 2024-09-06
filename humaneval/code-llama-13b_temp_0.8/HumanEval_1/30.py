from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    paren_string = paren_string.replace(' ', '')

    if len(paren_string) == 0:
        return result

    start_idx = 0
    for idx in range(1, len(paren_string)):
        left, right = paren_string[:idx], paren_string[idx:]
        if (left.count('(') == left.count(')')) and right.count('(') == right.count(')'):
            continue

        start_idx = idx
        break

    result.append(paren_string[:start_idx])
    result += separate_paren_groups(paren_string[start_idx:])
    return result

