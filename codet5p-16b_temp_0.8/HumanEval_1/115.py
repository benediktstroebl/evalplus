from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if len(paren_string) < 2:
        return []
    paren_strings = separate_paren_groups(paren_string[2:])
    brackets_stack = []
    result = []
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            brackets_stack.append(i)
        elif paren_string[i] == ')':
            if len(brackets_stack) == 0:
                return []
            start = brackets_stack.pop()
            if len(brackets_stack) == 0:
                result.append(paren_string[start: i + 1])
    return result + paren_strings
