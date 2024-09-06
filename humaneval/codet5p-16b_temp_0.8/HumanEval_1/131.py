from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if paren_string == '':
        return []
    else:
        if paren_string[0] == '(':
            groups = []
            sub_groups = separate_paren_groups(paren_string[1:])
            if sub_groups == []:
                return [paren_string[0]]
            else:
                for sub in sub_groups:
                    groups.append(paren_string[0] + sub)
                return groups
        else:
            return separate_paren_groups(paren_string[1:])
