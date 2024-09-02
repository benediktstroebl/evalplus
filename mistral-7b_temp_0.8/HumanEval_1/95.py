from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    def _separate(paren_string: str) -> List[str]:
        if len(paren_string) == 0:
            return []

        left_count = paren_string.count("(")
        right_count = paren_string.count(")")

        if left_count == right_count:
            return [paren_string] + _separate("")
        elif left_count > right_count:
            return [paren_string[0] + x for x in _separate(paren_string[1:])]
        elif left_count < right_count:
            return [y + paren_string[0] for y in _separate(paren_string[1:])]

    return _separate(paren_string)

