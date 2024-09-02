from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Brute force solution - O(n^2)
    # result = []
    # for i in range(len(paren_string)):
    #     for j in range(i + 1, len(paren_string) + 1):
    #         substring = paren_string[i:j]
    #         if _balanced_paren(substring):
    #             result.append(substring)
    # return result

