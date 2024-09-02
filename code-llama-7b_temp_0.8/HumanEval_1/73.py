from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Dictionary to keep track of all the parenthesis along with their count.
    paren_dict = {")": 0, "(": 0}
    # List to store all the groups
    output = []
    temp_string = ""

    for i in paren_string:
        # If i is a paren then we will update the dictionary and if its not we will add it to temp string
        if i in paren_dict:
            paren_dict[i] += 1
            if i == ")":
                temp_string += i
        else:
            temp_string += i

        # If count of all parenthesis is zero then we have a complete group
        if sum(paren_dict.values()) == 0:
            output.append(temp_string)
            temp_string = ""
            paren_dict = {")": 0, "(": 0}

    return output

