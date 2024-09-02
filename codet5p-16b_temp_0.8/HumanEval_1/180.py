from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if not paren_string:
        return []

    stack = [paren_string]
    groups = []

    while stack:
        current_string = stack.pop()

        if current_string[0] == '(':
            current_string = current_string[1:]
            continue
        if current_string[-1] == ')':
            current_string = current_string[:-1]
            continue

        if '(' in current_string:
            start = current_string.index('(')
            end = start + 1

            while '(' in current_string:
                end = current_string.index('(')
                current_string = current_string[:start] + current_string[end:]
                start = current_string.index('(')

            current_string = current_string[:start] + current_string[end:]

        if ')' in current_string:
            start = current_string.index(')')
            end = start + 1

            while ')' in current_string:
                end = current_string.index(')')
                current_
