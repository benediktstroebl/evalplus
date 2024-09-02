from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # create a list of open and close parenthesis for each group
    paren_group_list = paren_string.split("()")
    # strip each group of their parenthesis
    paren_group_list = [group.strip() for group in paren_group_list]
    # remove empty groups from the list
    paren_group_list = [group for group in paren_group_list if group]
    # add the empty groups back at the end
    paren_group_list.append("")
    # return the paren groups in a list
    return paren_group_list

