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

    current_start_index = 0
    c_stack = []
    paren_groups = []

    for i, c in enumerate(paren_string):
        if c == '(':
            c_stack.append(i)
        elif c == ')':
            if c_stack:
                current_start_index = c_stack.pop()
                end_index = i + 1
                if c_stack:
                    end_index = c_stack[-1]
                paren_groups.append(paren_string[current_start_index:end_index])
                continue
            else:
                raise ValueError('Current stack is empty but we are trying to close a paren at index {}'.format(i))

    if c_stack:
        last_open_paren = c_stack.pop()
        raise ValueError('We are missing a close paren at index {}'.format(last_open_paren))

    return paren_groups

