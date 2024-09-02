from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # will start with an empty string
    paren_group = ""
    # final list of groups
    final_list = []
    # paren_group_flag is 1 if a balanced group is found, 0 if not
    paren_group_flag = 0

    for char in paren_string:
        if char in "()":
            if char == "(":
                if paren_group_flag == 0:
                    paren_group = "("
                    paren_group_flag = 1
                elif paren_group_flag == 1:
                    paren_group += "("
            elif char == ")":
                if paren_group_flag == 0:
                    continue
                else:
                    paren_group += ")"
                    if paren_group.count("(") == paren_group.count(")"):
                        paren_group_flag = 0
                        final_list.append(paren_group)
                        paren_group = ""

    return final_list

