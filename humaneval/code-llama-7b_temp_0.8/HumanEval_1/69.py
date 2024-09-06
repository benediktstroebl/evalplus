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
    if len(paren_string) == 0:
        return []
    if len(paren_string) == 2:
        if paren_string == "()":
            return [paren_string]
        else:
            return []
    current_start = 0
    current_count = 0
    for i in range(0, len(paren_string)):
        current_char = paren_string[i]
        if current_char == "(":
            current_count += 1
        elif current_char == ")":
            current_count -= 1
        if current_count == 0:
            output_list.append(paren_string[current_start:i + 1])
            current_start = i + 1

    return output_list

