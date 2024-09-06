from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # your code here
    result = []
    paren_stack = []
    i = 0
    while i < len(paren_string):
        if paren_string[i] == "(":
            paren_stack.append(i)
        else:
            if paren_stack:
                paren_stack.pop()
                if not paren_stack:
                    result.append(paren_string[paren_stack[-1] + 1:i])
            else:
                return result
        i += 1
    return result

