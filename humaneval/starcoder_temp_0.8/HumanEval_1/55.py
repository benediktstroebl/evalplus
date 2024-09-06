from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    output_list = []

    def dfs(paren_string, output_list):
        if paren_string.count('(') == paren_string.count(')'):
            if paren_string == '':
                return output_list.append(''.join(paren_string))
            else:
                return dfs(paren_string[1:-1], output_list)
        else:
            return dfs(paren_string[1:-1], output_list)

    dfs(paren_string, output_list)

    return output_list
