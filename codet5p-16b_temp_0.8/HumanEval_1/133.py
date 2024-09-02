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
    current_group = []
    current_depth = 0
    max_depth = 0
    max_depth_index = 0
    paren_list = list(paren_string)
    for i in range(len(paren_list)):
        if paren_list[i] == '(':
            current_depth += 1
            if current_depth > max_depth:
                max_depth = current_depth
                max_depth_index = i
        if paren_list[i] == ')':
            current_depth -= 1
        if current_depth == 0:
            current_group = paren_list[:max_depth_index + 1]
            result.append(''.join(current_group))
            current_group = []
    return result
    

