from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if paren_string is None or len(paren_string) == 0:
        return []
    result = []
    cur_string = ''
    open_parens = 0
    for i in range(len(paren_string)):
        char = paren_string[i]
        if char == '(' or char == ')':
            if open_parens == 0:
                cur_string = char
            else:
                cur_string += char
            if char == '(':
                open_parens += 1
            else:
                open_parens -= 1
            if i == len(paren_string) - 1:
                result.append(cur_string)
                cur_string = ''
    return result
