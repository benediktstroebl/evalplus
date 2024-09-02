from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    def is_balanced(paren_string):
        stack = []
        for c in paren_string:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif c in [')', '}', ']']:
                try:
                    top_element = stack.pop()
                except IndexError:
                    return False
                if (top_element == '(' and c!= ')') or (top_element == '{' and c!= '}') or (top_element == '[' and c!= ']'):
                    return False

        return stack == []

    groups = []
    left_p = 0
    for i, char in enumerate(paren_string):
        if char == '(':
            left_p += 1
        elif char == ')':
            if left_p == 0:
                raise ValueError("You have too many closing parentheses")
            left_p -= 1
        elif char == ')':
            if left_p == 0:
                groups.append(paren_string[i:])
                break

    return groups

