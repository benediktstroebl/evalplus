from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # HINT1: Keep reading the input until you find an opening parenthesis.
    # HINT2: When you find a closing parenthesis, compare its "level" with level of the last opening brace.
    # HINT3: Keep reading the input until the level of the current closing brace is the same or lower than the
    # level of the first opening brace.

    result = []
    # Keep reading the input until you find an opening parenthesis.
    start = paren_string.find("(")

    while start != -1:
        # When you find a closing parenthesis, compare its "level" with level of the last opening brace.
        end = start + 1
        while paren_string[end] != ")" or paren_string[end - 1] != "(":
            end += 1

        # Keep reading the input until the level of the current closing brace is the same or lower than the
        # level of the first opening brace.
        level = 0
        while level <= start:
            end += 1
            if paren_string[end] == "(":
                level += 1
            elif paren_string[end] == ")":
                level -= 1

        # Add this block to the result.
        result.append(paren_string[start:end])

        # Keep reading the input until you find an opening parenthesis.
        start = paren_string.find("(", end)
    return result

