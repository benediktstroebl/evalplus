from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # create an empty list for the output
    out = []
    # create a stack for tracking the grouping
    s = []
    for c in paren_string:
        if c == "(":
            # add the ( to the stack
            s.append(c)
        elif c == ")":
            # if the stack is empty, then the current grouping is not balanced
            if not s:
                return []
            # if the stack is not empty, pop the stack until the ( is found
            while s:
                if s[-1] == "(":
                    # if the last char is (, pop it out and append it to the output
                    s.pop()
                    out.append("".join(s))
                    break
                else:
                    # if the last char is not (, pop it out and ignore it
                    s.pop()
    return out
