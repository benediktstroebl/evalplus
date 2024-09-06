from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    start_index = 0
    output = []
    for i, char in enumerate(paren_string):
        if char == "(":
            start_index = i
        elif char == ")" and start_index != 0:
            if not is_balanced_paren_group(paren_string[start_index:i + 1]):
                continue
            output.append(paren_string[start_index:i + 1])
            start_index = 0

    return output

