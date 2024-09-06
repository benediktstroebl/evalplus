from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    """
    Algorithm:
        1. Start with an empty stack and an empty list.
        2. Traverse the string. If the next character is an open brace, push it into the stack.
        3. If the next character is a close brace, pop the stack if the top element in the stack is an open brace.
        4. If the stack is empty, add the next character to the list.
        5. Repeat from step 2 until the stack is empty.
    """

    stack: list = []
    groups: list = []

    for ch in paren_string:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(ch)
        else:
            continue
        if len(stack) == 0:
            groups.append(ch)

    return groups

