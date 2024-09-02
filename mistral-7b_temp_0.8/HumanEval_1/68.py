from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    output_list = []
    current_paren_group = ""
    paren_group_count = 0

    for paren in paren_string:
        if paren == '(':
            paren_group_count += 1
        elif paren == ')':
            paren_group_count -= 1

        if paren_group_count == 0:
            current_paren_group += paren
        else:
            if current_paren_group != "":
                output_list.append(current_paren_group)
                current_paren_group = ""

    if current_paren_group != "":
        output_list.append(current_paren_group)

    return output_list

