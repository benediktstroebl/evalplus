from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    return_list = []
    temp_str = paren_string
    while temp_str:
        # find first open brace
        open_idx = temp_str.find("(")
        if open_idx == -1:
            # no more open braces found
            # grab the remaining chars and add it to the return list
            return_list.append(temp_str)
            break
        else:
            # check if the open brace is not closed
            if temp_str[open_idx + 1] == "(":
                # find the corresponding closing brace
                close_idx = open_idx + 1
                paren_level = 1
                while paren_level > 0:
                    # increment the index by 1
                    close_idx += 1
                    if temp_str[close_idx] == "(":
                        # increase the paren level
                        paren_level += 1
                    elif temp_str[close_idx] == ")":
                        # decrease the paren level
                        paren_level -= 1
                # remove the paren group from temp_str
                group_str = temp_str[:close_idx + 1]
                temp_str = temp_str[close_idx + 1:]
                # add the group to the return list
                return_list.append(group_str)
            else:
                # open brace is closed
                # get the group
                open_idx = temp_str.find("(")
                group_str = temp_str[:open_idx]
                return_list.append(group_str)
                temp_str = temp_str[open_idx:]
    return return_list

