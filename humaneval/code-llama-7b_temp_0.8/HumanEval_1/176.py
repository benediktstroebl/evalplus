from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # todo: please help me understand what's the difference between this code and the one in the book.
    # todo: book code returns [(),(())]
    paren_stack = []
    str_list = []
    for char in paren_string:
        if char == '(':
            paren_stack.append('(')
            str_list.append('')
        elif char == ')':
            if paren_stack:
                paren_stack.pop()
                str_list[-1] += ')'
        else:
            str_list[-1] += char
    return str_list

