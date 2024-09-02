from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if len(paren_string) < 2 or not paren_string.startswith("(") or not paren_string.endswith(")"):
        return []

    left_paren_index = 0
    right_paren_index = 0
    left_braces = 0
    right_braces = 0
    for index, char in enumerate(paren_string):
        if char == "(":
            left_braces += 1
        elif char == ")":
            right_braces += 1

        if left_braces == right_braces:
            left_paren_index = index
            break

    for index, char in reversed(list(enumerate(paren_string))):
        if char == "(":
            left_braces += 1
        elif char == ")":
            right_braces += 1

        if left_braces == right_braces:
            right_paren_index = index
            break

    if left_paren_index == right_paren_index:
        return [paren_string]

    return [paren_string[0:left_paren_index + 1]] + separate_paren_groups(paren_string[left_paren_index + 1 : right_paren_index]) + separate_paren_groups(paren_string[right_paren_index + 1:])

