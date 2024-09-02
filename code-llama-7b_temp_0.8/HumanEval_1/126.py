from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    def paren_balance_check(paren_string):
        stack = []
        for paren in paren_string:
            if paren == '(':
                stack.append(paren)
            elif paren == ')':
                if len(stack) < 1:
                    return False
                stack.pop()
        return len(stack) == 0

    open_paren_indices = []
    for i, c in enumerate(paren_string):
        if c == '(':
            open_paren_indices.append(i)
        elif c == ')':
            if len(open_paren_indices) > 0:
                start_index = open_paren_indices.pop()
                end_index = i
                paren_list.append(paren_string[start_index: end_index + 1])
            else:
                raise Exception("Improperly nested parens")

    if paren_balance_check(paren_string):
        return paren_list
    else:
        raise Exception("Improperly nested parens")

