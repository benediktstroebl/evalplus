from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # here is a recursive solution
    # the idea is to iterate through the string
    # if the char is '(' then call the function and append the result to the list
    # if the char is ')' return the list
    # if not either of the above then append the char to the list
    if not paren_string:
        return []

    def get_paren_groups(s, res):
        # iterate through the string
        for char in s:
            # if the char is '(' then call the function and append the result to the list
            if char == '(':
                res.append('(')
                get_paren_groups(s[1:], res)
            # if the char is ')' return the list
            elif char == ')':
                res.append(')')
                return res
            # if not either of the above then append the char to the list
            else:
                res.append(char)

    return get_paren_groups(paren_string, [])

