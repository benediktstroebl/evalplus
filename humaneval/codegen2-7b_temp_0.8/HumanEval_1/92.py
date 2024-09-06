from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def _inner_recurse(paren_string: str, position: int, output: List[str]):
        if position == len(paren_string):
            return output

        if paren_string[position] == '(':
            return _inner_recurse(paren_string, position + 1, output)
        output.append(paren_string[position])
        return _inner_recurse(paren_string, position + 1, output)

    return _inner_recurse(paren_string, 0, [])
