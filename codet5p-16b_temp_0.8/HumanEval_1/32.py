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
        return [paren_string]

    return_list = []
    current_group = ""
    is_balance = True
    is_nested = False
    for i in paren_string:
        if i == '(':
            if is_balance:
                is_balance = False
                is_nested = True
        elif i == ')':
            if is_nested:
                is_nested = False
                is_balance = True
                current_group += i
            else:
                current_group += i

    if current_group!= "":
        return_list.append(current_group)
    return_list += separate_paren_groups(paren_string[len(current_group):])

    return return_list

