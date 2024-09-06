from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_stack = []  # record of matching parens
    separated_groups = []  # list of strings that separate groups
    # keep track of which position we are filling in with matching parens
    i = 0
    while i < len(paren_string):
        if paren_string[i] == '(':
            paren_stack.append('(')
        elif paren_string[i] == ')':
            if len(paren_stack) == 0:  # paren group is finished
                separated_groups.append(paren_string[:i])
                i += 1
                continue
            paren_stack.pop()
        i += 1
    separated_groups.append(paren_string[i:])
    return separated_groups

