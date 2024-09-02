from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    def balanced(string: str) -> bool:
        stack = []
        for char in string:
            if char == "(":
                stack.append(char)
            if char == ")" and len(stack)!= 0:
                stack.pop()
        return len(stack) == 0

    parentheses = []
    idx = 0
    while idx < len(paren_string):
        if paren_string[idx] == "(":
            substring = ""
            idx += 1
            while idx < len(paren_string) and paren_string[idx]!= ")":
                substring += paren_string[idx]
                idx += 1
            if idx < len(paren_string) and paren_string[idx] == ")":
                substring += ")"
                idx += 1
            if balanced(substring):
                parentheses.append(substring)
        else:
            idx += 1
    return parentheses

