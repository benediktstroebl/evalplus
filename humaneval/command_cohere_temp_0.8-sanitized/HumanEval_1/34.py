from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    open_braces = ''
    close_braces = ''
    paren_list = []

    for char in paren_string:
        if char == '(':
            open_braces += char
        elif char == ')':
            close_braces += char
        elif open_braces:
            open_braces += char
        elif close_braces:
            close_braces += char
        elif char != ' ':
            paren_list.append(open_braces + close_braces)
            open_braces = ''
            close_braces = ''

    # Handle potential remaining open and close braces
    if open_braces:
        paren_list.append(open_braces)
    if close_braces:
        paren_list.append(close_braces)

    return paren_list