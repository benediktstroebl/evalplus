from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result_list = []
    left_open = True
    p_stack = []
    i = 0
    while i < len(paren_string):
        if paren_string[i] == "(":
            p_stack.append(paren_string[i])
            left_open = True
        elif paren_string[i] == ")":
            if left_open:
                p_stack.pop()
                left_open = False
            else:
                result_list.append(paren_string[:i + 1])
                i += 1
        elif paren_string[i] != " ":
            i += 1
    if left_open:
        result_list.append(paren_string)
    return result_list

