from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # initialise list of results
    result = []

    # the stack to store the opening braces
    stack = []

    # empty string to store the result
    res = ''

    for i in paren_string:
        # check if opening bracket
        if i == '(':
            stack.append(i)
        # check if closing bracket
        elif i == ')':
            # if stack is empty, then an unbalanced closing bracket
            if not stack:
                result.append(res)
                res = ''
                continue
            # otherwise, pop the last character from the stack and append to res
            # check if it's an unbalanced closing bracket
            elif stack.pop() != '(':
                result.append(res)
                res = ''
                continue
        res += i

    if res != '':
        result.append(res)

    return result

