from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    def check_if_balanced(string):
        """
        return True if string is balanced
        return False if string is not balanced
        """
        stack = []
        for char in string:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()

        if len(stack) == 0:
            return True
        else:
            return False

    paren_strings = []
    balance_flag = True

    while balance_flag:
        start_pos = paren_string.find('(')
        if start_pos == -1:
            balance_flag = False
        else:
            end_pos = paren_string.find(')')
            if check_if_balanced(paren_string[start_pos:end_pos + 1]):
                paren_strings.append(paren_string[start_pos:end_pos + 1])
                paren_string = paren_string[end_pos + 1:]
            else:
                return None
    return paren_strings

