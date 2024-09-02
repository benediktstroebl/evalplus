from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # begin with an empty list and a empty string
    list_of_strings = []
    current_string = ""
    # start at 0 and loop to the length of the string - 1 (so we don't go past the last character)
    for i in range(0, len(paren_string) - 1):
        # check if the current character is an opening brace. If it is, append it to the current string
        if paren_string[i] == "(":
            current_string += "("
        # if the character isn't an opening brace, check if it's a closing brace
        elif paren_string[i] == ")":
            # if it is, append it to the current string
            current_string += ")"
            # check if the current string is balanced (every opening brace has a corresponding closing brace).
            # if it is, append the current string to the list of strings
            if is_balanced(current_string):
                list_of_strings.append(current_string)
                # reset the current string to be empty
                current_string = ""
    # return the list of strings
    return list_of_strings

