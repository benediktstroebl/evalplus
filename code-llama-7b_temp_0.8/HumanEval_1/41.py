from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def _separate_paren_groups(paren_string):
        return __separate_paren_groups(paren_string, 0, len(paren_string) - 1, [])

    def __separate_paren_groups(paren_string, left, right, result):
        if left > right:
            return result
        if paren_string[left] == '(':
            left += 1
        if paren_string[right] == ')':
            right -= 1
        if left < right:
            left, right = __separate_paren_groups(paren_string, left, right, result)
        if left == right:
            return left + 1, right, result + [paren_string[left:right + 1]]
        return left, right, result

    return _separate_paren_groups(paren_string)

