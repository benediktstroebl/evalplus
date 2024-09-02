from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # use stack to keep track of free parentheses
    stack = []
    # output list
    group_list = []

    i = 0
    while i < len(paren_string):
        char = paren_string[i]
        if char == '(':
            stack.append(char)
        elif char == ')':
            # its balanced, so pop from stack until we see a matching (
            while not stack:
                # make sure the new char is not closed, or while it is
                open_char = stack.pop()
                if open_char != '(':
                    raise IndexError('no matching ( for %s' % char)

                # match, so get the new string and add it to the list of strings
                new_string = paren_string[i + 1:len(paren_string) - i]
                group_list.append(new_string)
                # increment the index to the next char
                i += len(new_string) + 1
            # if before we found a ) we don't have an open (
            else:
                raise IndexError('unbalanced (')
        else:
            # just a character
            i += 1

    return group_list

