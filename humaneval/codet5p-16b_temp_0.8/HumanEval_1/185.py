from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if paren_string.count('(')!= paren_string.count(')'):
        raise Exception('Parentheses do not match')
    else:
        separated_paren_groups = []
        current_group = ''
        for paren in paren_string:
            current_group += paren
            if paren == '(':
                if paren_string.count('((') == 1:
                    current_group += ')'
                else:
                    continue
            elif paren == ')':
                if paren_string.count(')(') == 1:
                    current_group += '('
                else:
                    continue
            separated_paren_groups.append(current_group)
            current_group = ''
        return separated_paren_groups

