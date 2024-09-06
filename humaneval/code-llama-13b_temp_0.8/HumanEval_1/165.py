from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack = []
    for char in paren_string:
        if char in ('(', ')'):
            if char == '(':
                stack.append(char)
            elif stack:
                if stack.pop() != '(':
                    raise ValueError("Input string is not balanced")

    while stack:
        if stack[-1] == '(':
            raise ValueError("Input string is not balanced")
        stack.pop()
    return [paren_string[start + 1:stop] for start, stop in zip([index for index, char in enumerate(paren_string) if
                                                                 char == '('] + [len(paren_string)],
                                                                [index for index, char in enumerate(paren_string) if
                                                                 char == ')'])]

