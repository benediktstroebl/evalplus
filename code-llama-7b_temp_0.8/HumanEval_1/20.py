from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # a stack to store opening parens' positions
    stack: List[int] = []
    # a list to store the output
    result: List[str] = []

    for i, paren in enumerate(paren_string):
        # if this is an opening paren, add its position to stack
        if paren == "(":
            stack.append(i)
        # if this is a closing paren
        elif paren == ")":
            # pop the last opening paren's position from stack
            start = stack.pop()
            # add the substring to result list
            result.append(paren_string[start: i + 1])

    return result

