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
    last_index = 0
    for index, ch in enumerate(paren_string):
        if ch == "(":
            stack.append(index)
        elif ch == ")":
            start_index = stack.pop()
            group = paren_string[start_index: index + 1]
            yield group
            last_index = index
    assert not stack
    group = paren_string[last_index:]
    yield group

