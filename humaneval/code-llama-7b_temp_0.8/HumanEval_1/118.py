from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Problem can be solved using stack
    # Here we'll use a queue
    groups = []
    q = []
    open_count = 0
    for char in paren_string:
        if char == "(":
            open_count += 1
            q.append(char)
        if char == ")":
            open_count -= 1
            q.append(char)
            if open_count == 0 and q:
                groups.append("".join(q))
                q.clear()
    return groups

