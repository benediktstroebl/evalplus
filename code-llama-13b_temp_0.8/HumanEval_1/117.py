from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # base case: 0 length string
    if len(paren_string) == 0:
        return []

    # setup:
    new_paren_string = ""
    paren_group_list = []

    # loop over the input string
    for char in paren_string:
        # if open brace, add it to new_paren_string
        if char == "(":
            new_paren_string += char
        # if close brace, remove last open brace, and continue
        if char == ")":
            new_paren_string = new_paren_string[:-1]
            # add new_paren_string to paren_group_list
            paren_group_list.append(new_paren_string)
            new_paren_string = ""

    # clean up empty entries in the list
    paren_group_list = [i for i in paren_group_list if i != ""]
    # return the result
    return paren_group_list

