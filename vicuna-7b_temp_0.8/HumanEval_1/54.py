from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def count_open_braces(s):
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
        return count

    def count_nested_parens(s):
        count = 0
        last_char = s[-1]
        for i in range(len(s)-1, -1, -1):
            if s[i] == '(' and s[i+1] == last_char:
                count += 1
            elif s[i] == last_char and s[i+1:] == s[i:i+1]:
                count += 1
        return count

    def separate_nested_parens(s):
        open_parens = 0
        nested = []
        for char in s:
            if char == '(':
                open_parens += 1
            elif char == ')':
                open_parens -= 1
            elif open_parens == 0:
                nested.append(char)
            elif open_parens == 1 and count_nested_parens(nested[-1]) > 0:
                nested[-1] += char
            elif count_nested_parens(nested[-1]) > 0:
                nested[-1] += char
                open_parens += 1
        return nested

    def split_paren_groups(s):
        nested = []
        open_parens = 0
        for char in s:
            if char == '(':
                open_parens += 1
            elif char == ')':
                open_parens -= 1
            elif open_parens == 0:
                nested.append(char)
            elif count_open_braces(nested[-1]) > 0:
                nested[-1] += char
                open_parens += 1
            elif count_open_braces(nested[-1]) == 0 and count_nested_parens(nested[-1]) > 0:
                nested[-1] += char
                open_parens += 1
        return nested

    return split_paren_groups
