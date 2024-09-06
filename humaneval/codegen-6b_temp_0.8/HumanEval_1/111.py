from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Split the string into substrings separated by parentheses
    parens = paren_string.split('(')

    # Separate each substring into groups separated by close and open parentheses
    groups = []
    for group in parens:
        group_number = 1
        open_count = 0
        close_count = 0
        for c in group:
            if c == '(':
                open_count += 1
            elif c == ')':
                close_count += 1
            if open_count == close_count:
                groups.append(group[:close_count + 1])
                break
            group_number += 1

    # Return the separated strings
    return groups

