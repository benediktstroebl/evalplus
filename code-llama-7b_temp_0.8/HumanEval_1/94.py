from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    groups = []
    paren_stack = []

    for paren in paren_string:
        if paren == "(":
            paren_stack.append(paren)
        elif paren == ")":
            if len(paren_stack) == 0:
                continue
            elif paren_stack[-1] == "(":
                paren_stack.pop()
                groups.append("".join(paren_stack))
                paren_stack = []
            else:
                paren_stack.append(paren)
        else:
            paren_stack.append(paren)

    if len(paren_stack) != 0:
        raise Exception(f"Parenthesis mismatch: {paren_stack}")

    return groups

