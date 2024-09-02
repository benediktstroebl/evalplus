from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # YOUR CODE GOES BELOW
    group_list = []
    start_index = 0
    end_index = 0
    for i in range(len(paren_string)):
        if paren_string[i] == "(":
            start_index = i
        elif paren_string[i] == ")":
            end_index = i
            sub_group = paren_string[start_index:end_index+1]
            group_list.append(sub_group)
            start_index = end_index + 1

    return group_list

