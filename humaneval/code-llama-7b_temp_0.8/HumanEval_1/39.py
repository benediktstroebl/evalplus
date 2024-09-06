from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if len(paren_string) == 0:
        return []
    elif len(paren_string) == 2:
        if paren_string[0] == '(' and paren_string[-1] == ')':
            return [paren_string]
        else:
            return []
    else:
        list_of_strings = []
        count_l_paren = 0
        start = 0
        for i in range(len(paren_string)):
            if paren_string[i] == '(':
                count_l_paren += 1
            elif paren_string[i] == ')':
                count_l_paren -= 1
            if count_l_paren == 0:
                list_of_strings.append(paren_string[start: i+1])
                start = i + 1
        return list_of_strings

