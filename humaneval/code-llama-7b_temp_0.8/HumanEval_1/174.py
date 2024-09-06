from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # get rid of the spaces by replacing them with nothing
    clean_string = paren_string.replace(" ", "")

    # creating a list to store our results
    separate_list = []

    # looping through our string
    for character in clean_string:

        # if we find a "(" we add it to a new string
        if character == "(":
            new_string = ""
            new_string += character

        # else if we find a ")" we check to see if our string exists, if it does we append it to our list
        elif character == ")":
            if new_string:
                separate_list.append(new_string)

        # else we just append that character to our new string
        else:
            new_string += character

    return separate_list

