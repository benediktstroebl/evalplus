from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    """
    Youtube tutorial to refer to:
    https://www.youtube.com/watch?v=9-9Jjy6Fm1w
    """
    def is_balance(paren_str):
        stack = []
        for char in paren_str:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False
    def remove_left_most_paren(paren_str):
        i = 0
        while paren_str[i] != '(' and i < len(paren_str):
            i += 1
        if i == len(paren_str):
            return paren_str[1:]
        return paren_str[i+1:]
    paren_groups = []
    i = 0
    while i < len(paren_string):
        #print(paren_string[i:])
        paren_str = p
