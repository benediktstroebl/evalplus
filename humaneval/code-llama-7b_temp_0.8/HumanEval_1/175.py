from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # find out if it has a balanced count of parenthesis
    paren_count = 0
    for char in paren_string:
        if char == '(':
            paren_count += 1
        if char == ')':
            paren_count -= 1
    if paren_count != 0:
        raise SyntaxError('Unbalanced parenthesis')

    #  Find out the start and end indices of the parenthesis groups
    paren_groups = []
    in_paren = False
    start_index = -1
    end_index = -1
    for i in range(0, len(paren_string)):
        if paren_string[i] == '(':
            if in_paren:
                raise SyntaxError('Nested parenthesis')
            in_paren = True
            start_index = i
        if paren_string[i] == ')':
            in_paren = False
            end_index = i
            paren_groups.append([start_index, end_index])
    # Add the last paren group if it does not end with a parenthesis
    if in_paren:
        paren_groups.append([start_index, len(paren_string) - 1])

    # Get the indices of parenthesis and split it into list of strings
    return [''.join(list(s)) for s in zip(*paren_groups)]

