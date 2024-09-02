from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Initialize the output list
    out_lst = []
    # Initialize variables for tracking the count of open and closed parenthesis
    open_cnt = 0
    closed_cnt = 0
    # Initialize the temporary string
    tmp_str = ''

    # Iterate over the string character by character
    for i in paren_string:
        # Increment the counts for open and closed parentheses
        if i == '(':
            open_cnt += 1
        elif i == ')':
            closed_cnt += 1
        # Concatenate the character to the temporary string
        tmp_str += i

        # Check if the counts for open and closed parentheses match
        if open_cnt == closed_cnt:
            # Add the temporary string to the output list
            out_lst.append(tmp_str)
            # Clear the temporary string
            tmp_str = ''

    return out_lst

