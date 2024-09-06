from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Your implementation goes here
    nesting_level = 0
    left_open = False
    left_close = False
    right_open = False
    right_close = False
    result = []
    for char in paren_string:
        if char == '(':
            if not left_open:
                left_open = True
                left_close = False
            else:
                nesting_level += 1
                left_open = False
                right_open = False
        elif char == ')':
            if not right_close:
                right_open = True
                right_close = False
            else:
                nesting_level -= 1
                if nesting_level == 0:
                    result.append(paren_string[0:left_close])
                else:
                    left_open = True
                    left_close = False
                right_open = False
                right_close = False
        elif char == ' ':
            pass
    if not left_open:
        result.append(paren_string[0:left_close])
    else:
        result.append('')
    return result
