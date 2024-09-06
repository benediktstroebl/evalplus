from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    bracket_stack = []
    bracket_dict = {')': '(', ']': '[', '}': '{'}
    output_list = []
    for char in paren_string:
        if char in bracket_dict.keys():
            if bracket_dict[char] in bracket_stack:
                bracket_stack.pop()
            else:
                bracket_stack.append(char)
        else:
            if len(bracket_stack) == 0:
                output_list.append(char)
            else:
                bracket_stack.append(char)

    output_list.extend(bracket_stack[::-1])

    return output_list

