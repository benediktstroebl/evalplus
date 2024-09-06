from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # YOUR CODE HERE
    result = []
    index = 0
    for i in range(0, len(paren_string)):
        if i + 1 < len(paren_string) and paren_string[i + 1] == '(':
            result.append(paren_string[index:i + 1])
            index = i + 1
    return result

