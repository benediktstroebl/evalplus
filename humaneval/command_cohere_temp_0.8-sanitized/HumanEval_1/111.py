from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    open_braces = '('
    close_braces = ')'
    separated_groups = []
    current_group = ''

    for char in paren_string:
        if char == open_braces:
            current_group += char
        elif char == close_braces:
            if not current_group.count(open_braces):
                separated_groups.append(current_group)
                current_group = ''
        else:
            current_group += char

    # Handle the last group
    if current_group:
        separated_groups.append(current_group)

    return separated_groups