from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # group_list = []
    # current_index = 0
    # nested_count = 0
    # while current_index < len(paren_string):
    #     if paren_string[current_index] == "(":
    #         nested_count += 1
    #     elif paren_string[current_index] == ")":
    #         nested_count -= 1
    #     if nested_count == 0:
    #         group_list.append(paren_string[current_index])
    #     current_index += 1
    # return group_list
    return [i.replace(" ", "") for i in paren_string.split(")(")]

