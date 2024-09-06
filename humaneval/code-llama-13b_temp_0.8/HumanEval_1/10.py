from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Make a new list
    paren_list = list(paren_string)
    # Get rid of all of the spaces
    paren_list = [item for item in paren_list if item != " "]
    # Make an empty list to return
    ret_list = []
    # Make a var to keep track of how many you have seen
    seen = 0
    # Go through the list
    for i in range(len(paren_list)):
        # If you see an open paren
        if paren_list[i] == "(":
            # Add 1 to seen
            seen += 1
        # If you see a close paren
        elif paren_list[i] == ")":
            # Subtract 1 from seen
            seen -= 1
        # If you have seen 0 seen parens
        if seen == 0:
            # Add that to your ret_list
            ret_list.append("".join(paren_list[: i + 1]))
            # Reset paren_list to what is left
            paren_list = paren_list[i + 1 :]
            # Reset seen to 0
            seen = 0

    # Return your list
    return ret_list
