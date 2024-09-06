from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.replace(" ", "")
    paren_open_count = 0
    paren_string_list = []

    for char in paren_string:
        if char == "(":
            paren_open_count += 1
        elif char == ")":
            paren_open_count -= 1
        if paren_open_count == 0 and char != ")":
            paren_string_list.append(paren_string[:paren_string.index(char) + 1])
            if char != ")":
                paren_string_list.append(paren_string[
                                         paren_string.index(char) + 1:])  # This is the tricky part!
            else:
                paren_string_list.append(paren_string[
                                         paren_string.index(char) + 1:paren_string.index(")")])

    return paren_string_list

