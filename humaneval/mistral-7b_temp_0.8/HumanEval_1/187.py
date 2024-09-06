from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    def is_valid(paren_string: str) -> bool:
        """
        The function takes a string as an input and checks if it is a valid parentheses string
        """
        if len(paren_string) % 2 != 0:
            return False
        for char in paren_string:
            if char not in "()":
                return False
        return True

    def make_valid(paren_string: str) -> str:
        """
        The function takes a string as an input and returns a valid parentheses string
        """
        idx = 0
        while idx < len(paren_string):
            if paren_string[idx] == "(":
                idx += 1
                continue
            else:
                new_string = paren_string[idx] + paren_string[idx - 1]
                paren_string = new_string + paren_string[idx + 1:]
                idx -= 2
        return paren_string

    def recursive_split(paren_string: str, stack
