from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # We have a stack of open parens and a list of strings to build.
    stack = []
    result = []
    # We don't know whether we've seen an open paren or not (yet), so we start with an empty string.
    substring = ''
    for c in paren_string:
        # If we've seen a closed paren, add it to the list and append to the substring.
        if c == ')':
            result.append(substring)
            substring = ''
            stack.pop()
        # If we see an open paren, add it to the stack
        elif c == '(':
            stack.append(c)
        elif c != ' ':
            substring += c
    # At this point we've added all the elements to the result and substring, so we add the last one.
    result.append(substring)
    return result

