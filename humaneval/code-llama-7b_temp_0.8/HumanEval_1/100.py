from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result: List[str] = []
    # your code here
    paren_string = paren_string.replace(" ", "")
    current_group = []

    for char in paren_string:
        if char == "(":
            current_group.append(char)
        elif char == ")":
            if len(current_group) == 0:
                return []
            else:
                current_group.pop()
                if len(current_group) == 0:
                    result.append("".join(current_group))
                    current_group = []

    return result

