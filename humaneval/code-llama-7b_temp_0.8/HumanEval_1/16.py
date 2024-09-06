from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # initiate variables
    i = 0
    list_result = []
    paren_string = paren_string.replace(" ", "")

    # while not reaching the end
    while i != len(paren_string):
        start = i
        current = paren_string[i]
        open_parentheses = 0
        # count the parenthesis
        while current != ')':
            if current == '(':
                open_parentheses += 1
            current = paren_string[i + 1]
            i += 1
        # add to list the result
        list_result.append(paren_string[start:i + 1])
        i += 1
    return list_result

