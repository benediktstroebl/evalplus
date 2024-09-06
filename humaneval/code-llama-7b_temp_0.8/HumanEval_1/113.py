from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    "*** YOUR CODE HERE ***"
    # Empty string -> empty list
    if paren_string == '':
        return []
    # (...()
    if paren_string[-1] == ')':
        return [paren_string] + separate_paren_groups(paren_string[:-1])
    # ()...)
    if paren_string[0] == '(':
        return [paren_string[1:]] + separate_paren_groups(paren_string[1:])

    start = 0
    while start < len(paren_string) and paren_string[start] != '(':
        start += 1
    end = start + 1
    while end < len(paren_string) and paren_string[end] != ')':
        end += 1

    return separate_paren_groups(paren_string[:start]) + separate_paren_groups(paren_string[end + 1:])

