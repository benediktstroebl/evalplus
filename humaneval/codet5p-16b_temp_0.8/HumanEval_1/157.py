from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if paren_string == "":
        return []
    groups: List[str] = []
    current_group = []
    stack = []
    is_open = False
    for i in range(len(paren_string)):
        if paren_string[i] == '(' or paren_string[i] == ')':
            if is_open:
                if paren_string[i] == ')':
                    current_group.append(paren_string[i])
                    groups.append("".join(current_group))
                    current_group = []
                    is_open = False
                else:
                    stack.append(paren_string[i])
            else:
                current_group.append(paren_string[i])
                if paren_string[i] == '(':
                    is_open = True
    return groups

