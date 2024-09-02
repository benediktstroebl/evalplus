from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    braces = []
    open_braces = ['(', '[', '{']
    closed_braces = [')', ']', '}']
    # check for balanced brackets
    for i in range(len(paren_string)):
        if paren_string[i] in open_braces:
            braces.append(paren_string[i])
        if paren_string[i] in closed_braces:
            if len(braces) == 0:
                return []
            if open_braces[closed_braces.index(paren_string[i])] != braces.pop():
                return []
    # return separate braces
    if len(braces) != 0:
        return []
    res = []
    count = 0
    current = ''
    for i in range(len(paren_string)):
        if paren_string[i] != ' ':
            if paren_string[i] in open_braces:
                count += 1
            if paren_string[i] in closed_braces:
                count -= 1
            current += paren_string[i]
            if count == 0:
                res.append(current)
                current = ''
    return res

