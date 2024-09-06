from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # check if the string is empty and return an empty list
    if len(paren_string) == 0:
        return []
    # create a list to hold all the paren groups
    paren_groups = list()
    # create a list to hold the parens
    parens = list()
    # the open braces
    open_parens = ['(', '[', '{']
    # the closing braces
    close_parens = [')', ']', '}']
    # the matching parens
    pairs = {'(': ')', ')': '(', '[': ']', ']': '[', '{': '}', '}': '{'}
    # loop through the string
    for c in paren_string:
        # if the char is a paren
        if c in open_parens or c in close_parens:
            # if the paren is in the open braces
            if c in open_parens:
                # append the paren to the list
                parens.append(c)
            else:
                # the paren is in the close braces
                # check if the list is empty
                if len(parens) == 0:
                    # there is no open paren, something went wrong
                    return []
                # if the last paren is not the pair of this paren
                if parens[len(parens) - 1] != pairs[c]:
                    # something went wrong
                    return []
                # remove the paren
                parens.pop()
                # if the list is empty
                if len(parens) == 0:
                    # append the list of parens to the list of paren_groups
                    paren_groups.append(''.join(parens))
                    # clear the parens
                    parens.clear()
        else:
            # append the char to the list
            parens.append(c)
    # check if the list is not empty
    if len(parens) > 0:
        # something went wrong
        return []
    # return the list of paren groups
    return paren_groups

