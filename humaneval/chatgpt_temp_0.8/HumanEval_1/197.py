def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    stack = []
    for c in paren_string:
        if c == '(':
            stack.append(c)
        elif c == ')':
            stack.pop()
            if not stack:
                result.append(paren_string[:paren_string.index(c)+1])
                paren_string = paren_string[paren_string.index(c)+1:].lstrip()
    return result
