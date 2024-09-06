from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    """
    if not paren_string:
        return []

    opening_balance = 0
    temp_string = ''
    paren_list = []

    for char in paren_string:
        if char == '(':
            opening_balance += 1
            temp_string += char
        elif char == ')':
            opening_balance -= 1
            temp_string += char
        elif char == ' ':
            continue

        if opening_balance == 0:
            paren_list.append(temp_string)
            temp_string = ''
            opening_balance = 0

    if opening_balance > 0:
        paren_list.append(temp_string)

    return paren_list