from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    paren_stack = []
    word_start = 0
    for idx, character in enumerate(paren_string):
        if character == "(":
            paren_stack.append(idx)
        elif character == ")":
            if len(paren_stack) > 0:
                paren_stack.pop()
            else:
                result.append(paren_string[word_start: idx + 1])
                word_start = idx + 1

    return result if len(result) > 0 else [paren_string]

