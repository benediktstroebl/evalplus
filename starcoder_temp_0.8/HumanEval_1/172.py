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
    start_index: int = 0
    end_index: int = 0
    is_open_paren: bool = False

    for index in range(len(paren_string)):
        if paren_string[index] == "(":
            if is_open_paren:
                raise ValueError("paren string is not balanced")

            start_index = index
            is_open_paren = True

        elif paren_string[index] == ")":
            if not is_open_paren:
                raise ValueError("paren string is not balanced")

            end_index = index
            result.append(paren_string[start_index:end_index + 1])
            is_open_paren = False

        elif paren_string[index] == " ":
            if is_open_paren:
                raise ValueError("paren string is not balanced")

    if is_open_paren:
        raise ValueError("paren string is not balanced")

    return result

