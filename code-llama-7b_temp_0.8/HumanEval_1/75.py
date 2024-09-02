from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Split the string into characters
    char_list = list(paren_string)
    # Resultant list of all groups
    result_list = []
    # current group
    group = []
    # top of the stack
    stack = []

    for ch in char_list:
        if ch == '(':
            stack.append(ch)
            group.append(ch)
        elif ch == ')':
            if not stack or stack.pop() != '(':
                return []
            group.append(ch)
            if not stack:
                result_list.append(''.join(group))
                group = []

    return result_list

