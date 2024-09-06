from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Use a stack to track the open parens
    stack = []
    groups = []
    for symbol in paren_string:
        if symbol == ')':
            # Pop all open parens off the stack
            while len(stack) > 0 and stack[-1] != '(':
                groups.append(stack.pop())
            # Pop the open parenthesis off the stack
            stack.pop()
        elif symbol == '(':
            # Push the open parenthesis onto the stack
            stack.append(symbol)
    # At this point, the stack should be empty and the groups list should have all the groups
    while len(stack) > 0:
        groups.append(stack.pop())
    return groups

