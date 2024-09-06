from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # a stack to save '(' braces
    stack: List[str] = []
    # a list to save all the balanced groups
    lst: List[str] = []
    # a variable to save the group
    group: List[str] = []

    for char in paren_string:
        if char == '(':
            stack.append(char)
            group.append(char)
        elif char == ')':
            if len(stack) != 0:
                group.append(char)
                stack.pop()
                # when the stack is empty, all the group is balanced
                if len(stack) == 0:
                    lst.append("".join(group))
                    group = []
            else:
                # we have an unbalanced group
                return []

    return lst

