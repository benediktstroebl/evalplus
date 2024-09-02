from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if paren_string is None or paren_string == '':
        return []
    res = []
    open_list = []
    open_pairs = {'(': ')', '[': ']', '{': '}'}
    close_pairs = {')': '(', ']': '[', '}': '{'}
    for char in paren_string:
        if char in open_pairs:
            open_list.append(char)
        elif char in close_pairs:
            if close_pairs[char] == open_list[-1]:
                open_list.pop()
            else:
                return []
    if open_list:
        return []
    else:
        while True:
            index = paren_string.find('()')
            if index > 0:
                paren_string = paren_string[:index] + ')' + paren_string[index + 2:]
            else:
                break
        while True:
            index = paren_string.find('[]')
            if index > 0:
