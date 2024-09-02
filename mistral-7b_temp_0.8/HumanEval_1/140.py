from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # your code here

    paren_list = []
    for i in paren_string:
        paren_list.append(i)
    open_parentheses = []
    closed_parentheses = []
    left = 0
    right = 0
    string = ''
    for j in paren_list:
        if j == '(':
            open_parentheses.append(j)
            left += 1
            if len(open_parentheses) == left:
                string += '('
        if j == ')':
            closed_parentheses.append(j)
            right += 1
            if len(closed_parentheses) == right:
                string += ')'
        if j == ' ':
            string += ' '
    print(string)
    string_list = []
    i = 0
    while i < len(string):
        string_list.append(string[i:i + len(string[i:])])
        i += len(string[i:])
        if string[i:i
