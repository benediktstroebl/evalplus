from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if paren_string == "":
        return []

    new_string = paren_string[::-1]
    result = []
    curr_string = ""
    prev_char = new_string[0]

    for i in range(len(new_string)):
        if new_string[i] == "(" and prev_char == ")":
            curr_string = curr_string[::-1]
            result.append(curr_string)
            curr_string = ""

        elif new_string[i] == ")":
            curr_string = curr_string[::-1]
            result.append(curr_string)
            curr_string = ""

        elif new_string[i] == "(" and prev_char == "(" and len(curr_string) == 0:
            curr_string = curr_string + "("
        elif new_string[i] == "(" and prev_char == "(" and len(curr_string) > 0:
            curr_string = curr
