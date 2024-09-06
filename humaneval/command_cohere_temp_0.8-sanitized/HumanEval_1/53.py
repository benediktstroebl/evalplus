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
        elif open_braces != '':
            open_braces += char
            if open_braces == '()':
                paren_list.append(open_braces)
                open_braces = ''
            elif open_braces == '():':
                paren_list.append(open_braces)
                open_braces = ''
            elif open_braces == '((':
                paren_list.append('(')
                open_braces = ''
            elif open_braces == '(((':
                paren_list.append('(')
                open_braces = ''
            else:
                open_braces += char
        elif close_braces != '':
            close_braces += char
            if close_braces == '))':
                paren_list.append(close_braces)
                close_braces = ''
            elif close_braces == '()))':
                paren_list.append(close_braces)
                close_braces = ''
            elif close_braces == '))(':
                paren_list.append(close_braces)
                close_braces = ''
            elif close_braces == '))(())':
                paren_list.append(close_braces)
                close_braces = ''
            else:
                close_braces += char

    if open_braces != '':
        paren_list.append(open_braces)
    if close_braces != '':
        paren_list.append(close_braces)

    return paren_list