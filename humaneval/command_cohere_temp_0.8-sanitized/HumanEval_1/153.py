from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    open_count = close_count = 0
    output = []
    current_group = []

    for char in paren_string:
        if char == '(':
            open_count += 1
            current_group.append(char)
        elif char == ')':
            close_count += 1
            if open_count == close_count:
                output.append(''.join(current_group))
                open_count, close_count = 0, 0
            else:
                current_group.append(char)
        else:
            current_group.append(char)

    # Handle the last group
    if open_count != close_count:
        output.append(''.join(current_group))

    return output