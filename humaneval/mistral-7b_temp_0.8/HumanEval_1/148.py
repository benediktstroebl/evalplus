from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def find_opening_brace(paren_string: str) -> int:
        i = 0
        for char in paren_string:
            if char == "(":
                i += 1
            elif char == ")":
                i -= 1
            if i < 0:
                return i
        return i

    def check_closing_brace(paren_string: str, index: int) -> bool:
        i = 0
        for char in paren_string[index:]:
            if char == "(":
                i += 1
            elif char == ")":
                i -= 1
            if i < 0:
                return False
        return True

    def find_next_closing_brace(paren_string: str, index: int) -> int:
        i = index
        for char in paren_string[i:]:
            if char == ")":
                i += 1
            elif char == "(":
                i -= 1
            if i < index:
                return i
       
