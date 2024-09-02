from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    open_parens = []
    open_parens_to_close_index = []
    for i, char in enumerate(paren_string):
        if char == '(':
            open_parens.append(i)
        elif char == ')' and len(open_parens)!= 0:
            open_parens_to_close_index.append(open_parens.pop())
    print(open_parens_to_close_index)
    output = []
    curr_output = ''
    for i, char in enumerate(paren_string):
        if i in open_parens_to_close_index:
            output.append(curr_output)
            curr_output = ''
        else:
            curr_output += char

    return output

