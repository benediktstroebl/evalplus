from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # list of groups of parentheses
    paren_groups: List[str] = []

    # build paren_groups by partitioning the string, starting from the leftmost
    index: int = 0
    while index < len(paren_string):
        # start of a new group
        paren_group: str = ""
        # count the number of opening braces found so far
        num_open_braces: int = 0

        # keep adding to the group until the group is balanced
        while index < len(paren_string):
            # if we find an open brace, increment the number of opening braces
            if paren_string[index] == "(":
                num_open_braces += 1
            # if we find a close brace, decrement the number of opening braces
            elif paren_string[index] == ")":
                num_open_braces -= 1
                # if the number of opening braces is 0, the group is balanced
                if num_open_braces == 0:
                    # stop adding to the group and move on to the next group
                    break

            # add the current character to the group
            paren_group += paren_string[index]

            # increment the index
            index += 1

        # add the balanced group to the list of groups
        paren_groups.append(paren_group)

    return paren_groups
