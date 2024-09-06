from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Hint: try to use stack to solve this problem
    out, stack, current = [], [], ""
    for c in paren_string:
        if c == " ":
            continue
        if c == "(":
            stack.append(c)
            current += c
        if c == ")":
            current += c
            stack.pop()
            if not stack:
                out.append(current)
                current = ""
    return out

