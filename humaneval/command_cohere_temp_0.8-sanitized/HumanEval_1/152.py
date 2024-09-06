from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    open_braces = '('
    close_braces = ')'
    output = []
    current_group = ''

    for char in paren_string:
        if char == open_braces:
            current_group += char
        elif char == close_braces:
            current_group += char
            if current_group == '()':
                output.append('')
            else:
                output.append(current_group)
                current_group = ''
        else:
            current_group += char

    if current_group:
        output.append(current_group)

    return output