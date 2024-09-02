from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack = []
    for i, char in enumerate(paren_string):
        if char == '(':
            stack.append(i)
        elif char == ')':
            open_index = stack.pop()
            start_index = open_index
            end_index = i
            while paren_string[start_index] == ' ':
                start_index -= 1
            while paren_string[end_index] == ' ':
                end_index += 1
            yield paren_string[start_index:end_index+1]
    return list(separate_paren_groups(paren_string))
