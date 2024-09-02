from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # dividing string into characters and converting to list
    paren_string_list = list(paren_string)
    # finding the number of opening and closing parenthesis
    open_parenthesis = paren_string_list.count("(")
    close_parenthesis = paren_string_list.count(")")

    # check for balanced parentheses
    if open_parenthesis != close_parenthesis:
        return ["Not balanced"]

    # initalize variables
    open_count, close_count, count = 0, 0, 0
    start_index = []

    for i in range(len(paren_string_list)):
        if paren_string_list[i] == "(":
            open_count += 1
            start_index.append(i)
        elif paren_string_list[i] == ")":
            close_count += 1
            if open_count == close_count and open_count > 0:
                end_index = i
                paren_string_list[start_index[-1]] = " "
                paren_string_list[end_index] = " "
                paren_string_list[start_index[count]] = " "
                count += 1
                start_index = []
                open_count, close_count = 0, 0

    # return all the values in a list
    return list(filter(None, "".join(paren_string_list).split()))

