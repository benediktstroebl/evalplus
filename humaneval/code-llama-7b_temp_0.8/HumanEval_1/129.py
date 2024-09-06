from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # initialize stack and list
    stack, groups = [], []

    # traverse string char by char
    for char in paren_string:
        # if it's left paren, append char to stack
        if char == '(':
            stack.append(char)
        # if it's right paren and stack is empty, list empty group and raise error
        elif char == ')':
            if not stack:
                raise Exception('invalid input')
            # pop char from stack and add it to list
            groups.append(stack.pop())
        # if it's another char, raise error
        else:
            raise Exception('invalid input')

    # if stack is not empty, raise error
    if stack:
        raise Exception('invalid input')

    return groups

