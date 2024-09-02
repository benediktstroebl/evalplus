from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def check_balance(open_brace: str, closed_brace: str) -> bool:
        """
        This helper function is used to check if the given open and closed braces are in a balanced group
        """
        if open_brace != closed_brace:
            return False
        return True

    def parse(string: str) -> List[str]:
        stack = []
        open_brace_count = 0
        for char in string:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack or not check_balance(stack[-2], stack[-1]):
                    raise ValueError("Unbalanced parentheses")
                stack.pop()
            elif char == ' ':
                pass
            else:
                raise ValueError("Invalid input")
        return stack

    def process(string: str) -> List[str]:
        string = "".join(string)
        return [s for s in parse(string) if not ' ' in s]

    return process(paren_string)
