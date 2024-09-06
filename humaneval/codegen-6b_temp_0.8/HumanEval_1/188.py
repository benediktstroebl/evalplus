from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    new_list = []
    if len(paren_string)==1:
        return [paren_string]
    for i in range(1, len(paren_string)):
        new_string = paren_string[:i]
        string_length = len(new_string)
        opened = 0
        for j in range(string_length):
            if new_string[j] == '(':
                opened += 1
            elif new_string[j] == ')':
                opened -= 1
            if opened == 0:
                new_list.append(new_string[:j+1])
    return new_list

