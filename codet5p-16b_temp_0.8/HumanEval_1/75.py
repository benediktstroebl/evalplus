from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    stack: List[str] = []

    def push_to_stack(item: str):
        if item == ')':
            opening = stack.pop()
            while opening!= '(':
                stack.append(opening)
                opening = stack.pop()
        elif item == '(':
            stack.append(item)
        else:
            stack.append(item)

    for item in paren_string:
        push_to_stack(item)

    output: List[str] = []
    while stack:
        output.append(stack.pop())

    return output
