from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def count_open_braces(s: str) -> int:
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
        return count

    def process(s: str) -> List[str]:
        open_brace_count = count_open_braces(s)
        result = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                result.append(s[i])
                i += 1
                while i < len(s) and count_open_braces(s[i:]) == open_brace_count:
                    result.append(s[i])
                    i += 1
            elif s[i] == ')':
                result.append(s[i])
                i += 1
                while i < len(s) and count_open_braces(s[i:]) < open_brace_count - 1:
                    result.append(s[i])
                    i += 1
            else:
                result.append('')
                i += 1
        return result

    return process(paren_string)
