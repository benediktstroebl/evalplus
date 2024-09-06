from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack = []
    result = []

    def parse_string(paren_string: str) -> List[str]:
        """
        You can use this function to parse the string in smaller chunks
        """
        for char in paren_string:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return result
                else:
                    result.append(''.join(stack))
                    stack.pop()
        return result

    result = parse_string(paren_string)
    return result
