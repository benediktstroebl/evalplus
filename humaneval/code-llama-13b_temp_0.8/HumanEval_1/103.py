from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # return separated groups
    paren_groups: List[str] = []
    # current index of group in paren_string
    group_start: int = 0
    for index in range(len(paren_string)):
        # check if character is a left or right parenthesis
        if paren_string[index] in '()':
            # check if character is left parenthesis
            if paren_string[index] == '(':
                # check if next character is right parenthesis
                if index < len(paren_string) - 1 and paren_string[index + 1] == ')':
                    # check if following right parenthesis is not the last character
                    if index < len(paren_string) - 2:
                        # check if next following character is not a right parenthesis
                        if paren_string[index + 2] != ')':
                            # append group to list
                            paren_groups.append(paren_string[group_start: index + 2])
                            # set group start to index of next character
                            group_start = index + 2
                    # append group to list
                    paren_groups.append(paren_string[group_start: index + 2])
                    # set group start to index of next character
                    group_start = index + 2
    # return list of groups
    return paren_groups

