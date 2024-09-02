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
    braces = "()[]"
    result = []

    for index, char in enumerate(paren_string):
        if char in braces:
            if char == "(":
                stack.append(char)
            else:
                if stack:
                    stack.pop()
        if char == ")":
            if stack:
                stack.pop()
            else:
                result.append(paren_string[index-len(paren_string) - 2: index])

    return result
