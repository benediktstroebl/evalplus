from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    index = 0
    while index < len(paren_string):
        level = 0
        start_index = index
        end_index = index
        while index < len(paren_string) and paren_string[index] != ')':
            if paren_string[index] == '(':
                level += 1
            elif paren_string[index] == ')':
                level -= 1
            index += 1
        if level == 0:
            result.append(paren_string[start_index:end_index + 1])
        index += 1

    return result

