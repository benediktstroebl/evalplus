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
        return [paren_string]

    ret = []
    current = []
    first_p = paren_string[0]
    current.append(first_p)

    for index, paren in enumerate(paren_string[1:]):
        if paren == '(':
            current.append('(')
        else:
            current.pop()
            if current == []:
                ret.append(''.join(current))
                current = [paren]
            else:
                if paren == ')':
                    ret.append(''.join(current))
                    current = [')']
                else:
                    current.append(paren)
    ret.append(''.join(current))
    return ret

