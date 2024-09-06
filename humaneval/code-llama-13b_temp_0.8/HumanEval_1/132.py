from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    open_braces = '({['
    close_braces = ')}]'
    reversed_braces = ')}]'[::-1]
    braces_stack = []
    current_string = ''
    separate_strings = []

    for i in paren_string:
        if i in open_braces:
            current_string += i
            braces_stack.append(i)
        elif i in close_braces:
            current_string += i
            reversed_index = reversed_braces.index(i)
            braces_stack.pop(reversed_index)
        elif i == ' ':
            continue
        else:
            raise SyntaxError("Unexpected character '{}' in paren string".format(i))

        if len(braces_stack) == 0:
            separate_strings.append(current_string)
            current_string = ''

    return separate_strings

