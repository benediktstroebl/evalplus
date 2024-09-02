from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if not paren_string or len(paren_string) == 0:
        return []

    stack = []
    index = 0
    result = []

    while index < len(paren_string):
        if paren_string[index] == "(":
            stack.append(index)
        elif paren_string[index] == ")":
            if len(stack) == 0:
                raise IndexError("Missing open brace")
            start = stack.pop()
            result.append(paren_string[start : index + 1])
        index += 1

    if stack:
        raise IndexError("Missing close brace")

    return result

