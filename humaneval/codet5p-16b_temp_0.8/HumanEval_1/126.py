from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    pass
    paren_stack = []
    group_list = []
    for c in paren_string:
        if c == "(":
            paren_stack.append(c)
        if c == ")":
            if not paren_stack:
                group_list.append("")
            else:
                paren_stack.pop()
                if not paren_stack:
                    group_list.append("".join(paren_stack))
                    paren_stack = []
                else:
                    group_list.append("".join(paren_stack))
                    paren_stack = []
    return group_list

