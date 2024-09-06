from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    output_list = []
    stack = []
    start = 0
    for i, char in enumerate(paren_string):
        if char == "(":
            stack.append("(")
            start = i
        elif char == ")":
            if len(stack) == 1:
                output_list.append(paren_string[start:i + 1])
                stack.pop()
            else:
                stack.pop()
    return output_list

