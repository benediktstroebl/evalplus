from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if not paren_string or paren_string.isspace():
        return []
    stack = []
    result = []
    index = 0
    for index in range(len(paren_string)):
        current_char = paren_string[index]
        if current_char == "(":
            stack.append(index)
        elif current_char == ")" and stack:
            last_open_brace = stack.pop()
            result.append(paren_string[last_open_brace : index + 1])
    return result

