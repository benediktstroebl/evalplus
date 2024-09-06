from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if paren_string == '':
        return []
    nested_paren_groups = []
    open_parens = 0
    close_parens = 0
    curr_group = ""
    paren_groups = []
    for char in paren_string:
        if char == '(':
            open_parens += 1
            curr_group += char
        elif char == ')':
            close_parens += 1
            curr_group += char
        elif char =='':
            if open_parens == close_parens:
                nested_paren_groups.append(curr_group)
                paren_groups.append(curr_group)
                curr_group = ""
                open_parens = 0
                close_parens = 0
    if curr_group!= "":
        nested_paren_groups.append(curr_group)
        paren_groups.append(curr_group)
    return nested_paren_groups
    raise NotImplementedError()

