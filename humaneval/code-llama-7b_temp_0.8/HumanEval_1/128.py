from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    res = []
    stack = []
    left_paren_index = 0
    right_paren_index = 0

    while left_paren_index < len(paren_string) and right_paren_index < len(paren_string):
        if paren_string[left_paren_index] == '(':
            if paren_string[right_paren_index] == ')':
                stack.append(paren_string[left_paren_index:right_paren_index + 1])
                left_paren_index = right_paren_index + 1
                right_paren_index = right_paren_index + 1

            else:
                right_paren_index += 1
        else:
            stack.append(paren_string[left_paren_index])
            left_paren_index += 1

    res.append(stack[-1])
    stack.pop()

    while len(stack) != 0:
        res.append(stack[-1])
        stack.pop()
    return res

