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
    current_group = []
    opening_bracket_count = 0
    for symbol in paren_string:
        if symbol == '(':
            opening_bracket_count += 1
            current_group.append(symbol)
        elif symbol == ')':
            opening_bracket_count -= 1
            if opening_bracket_count == 0:
                current_group.append(symbol)
                stack.append(''.join(current_group))
                current_group = []
            else:
                current_group.append(symbol)
        else:
            current_group.append(symbol)

    return stack

