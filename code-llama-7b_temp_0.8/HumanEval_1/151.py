from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if paren_string.find('(') == -1:
        return [paren_string]

    separated_strings = []
    for sub_str in paren_string.split('('):
        if sub_str == '':
            continue
        sub_str_end = 0
        for i in range(len(sub_str)):
            if sub_str[i] == ')':
                sub_str_end = i + 1
                break
        sub_str_end = len(sub_str) if sub_str_end == 0 else sub_str_end
        separated_strings.append(sub_str[0:sub_str_end])

        if sub_str_end < len(sub_str):
            separated_strings += separate_paren_groups(sub_str[sub_str_end:])

    return separated_strings

