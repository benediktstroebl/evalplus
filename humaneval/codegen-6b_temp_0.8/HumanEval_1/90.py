from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    my_list = []
    if len(paren_string) == 0:
        return my_list
    if len(paren_string) == 1:
        if paren_string == "()":
            return my_list
        else:
            return [paren_string]
    if paren_string[0] != "(":
        my_list.append(paren_string)
    else:
        i = 0
        while i < len(paren_string) and paren_string[i] != ")":
            if paren_string[i] == "(":
                my_list.append(paren_string[:i])
                paren_string = paren_string[i + 1 :]
                i = 0
            i += 1
        my_list.append(paren_string[:i])
    return separate_paren_groups(paren_string)

