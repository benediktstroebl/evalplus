from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    parentheses_group = []
    opening_parenthesis_found = False
    closing_parenthesis_found = False
    current_parenthesis_group = ''

    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            opening_parenthesis_found = True
            current_parenthesis_group += paren_string[i]

        if paren_string[i] == ')':
            closing_parenthesis_found = True
            current_parenthesis_group += paren_string[i]

        if (opening_parenthesis_found and not closing_parenthesis_found) or (closing_parenthesis_found and
                                                                              not opening_parenthesis_found):
            parentheses_group.append(current_parenthesis_group)
            current_parenthesis_group = ''

    return parentheses_group
