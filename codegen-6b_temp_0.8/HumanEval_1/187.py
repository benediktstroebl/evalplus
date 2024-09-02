from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # result = []
    # prev = ''
    # char = ''
    # for c in paren_string:
    #     if c == '(':
    #         if char != '':
    #             result.append(prev)
    #             prev = ''
    #         char = '('
    #     elif c == ')':
    #         if char == '(':
    #             result.append(prev)
    #             prev = ''
    #         char = ')'
    #     elif c == ' ':
    #         prev = prev + c
    #     else:
    #         prev = prev + c
    #     char = ''
    # result.append(prev)
    # return result

    # We solve this using a stack!
    result = []
    stack = []
    for c in paren_string:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                result.append('()')
            else:
                while len(stack) > 0:
                    last = stack.pop()
                    if last == '(':
                        return result

                    result.append(last + result.pop())
    return result
