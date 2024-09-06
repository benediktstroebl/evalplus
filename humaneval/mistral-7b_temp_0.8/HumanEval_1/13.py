from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    open_paren_stack = []
    final_list = []
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            open_paren_stack.append(i)
        if paren_string[i] == ')':
            if open_paren_stack:
                final_list.append(paren_string[open_paren_stack[-1] : i+1])
                open_paren_stack.pop()
            else:
                final_list.append(paren_string[i+1:])
    return final_list

