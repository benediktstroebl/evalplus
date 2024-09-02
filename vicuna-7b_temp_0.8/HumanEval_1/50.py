from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # convert the string to lowercase
    paren_string = paren_string.lower()

    # create an empty list to store the result
    result = []

    # loop through each character in the string
    for i, c in enumerate(paren_string):
        # if the current character is an opening parenthesis
        if c == '(':
            # if the previous character is not a closing parenthesis
            if i == 0 or paren_string[i-1] != ')':
                # append it to the result
                result.append(c)
            # ignore the current character
            i += 1
        # if the current character is a closing parenthesis
        elif c == ')':
            # if the current character is not followed by an opening parenthesis
            if i+1 < len(paren_string) and paren_string[i+1] != '(':
                # append it to the result
                result.append(c)
            # ignore the current character
            i += 1
        # if the current character is a space
        elif c == ' ':
            # ignore it
            pass

    # return the result
    return result