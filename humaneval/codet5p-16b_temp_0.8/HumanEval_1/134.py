from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    stack = []
    stack.append(paren_string)
    while stack:
        string = stack.pop()
        result = []
        level = 0
        for c in string:
            if c == '(':
                level += 1
            elif c == ')':
                level -= 1
            elif c =='' and level == 0:
                result.append(string[:string.index(c)])
                string = string[string.index(c)+1:]
                stack.append(string)
                break
        if not result:
            result.append(string)
    return result

