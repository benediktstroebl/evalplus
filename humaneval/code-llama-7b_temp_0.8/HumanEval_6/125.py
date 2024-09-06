from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # base case
    if paren_string == '':
        return []

    # recursion
    lparen_idx = paren_string.find('(')
    rparen_idx = paren_string.find(')')

    # if there are no parentheses in the string, then return 1
    if lparen_idx == -1:
        return [1]

    # if there is no corresponding right parenthesis to the left parenthesis, then return 1
    if rparen_idx == -1:
        return [1]

    # if there is a right parenthesis but no left parenthesis, then return 1
    if lparen_idx > rparen_idx:
        return [1]

    # if there is a left parenthesis but no corresponding right parenthesis, then return 1
    if lparen_idx < rparen_idx and paren_string[lparen_idx+1] == ')':
        return [1]

    # if there is a left parenthesis and a right parenthesis, and the right parenthesis is not immediately after the left
    # parenthesis, then return 1
    if lparen_idx < rparen_idx and paren_string[lparen_idx+1] != '(':
        return [1]

    # if there is a left parenthesis and a right parenthesis, and the right parenthesis is immediately after the left
    # parenthesis, then recurse on the substring with all the characters in between
    if lparen_idx < rparen_idx and paren_string[lparen_idx+1] == '(':
        return [1] + parse_nested_parens(paren_string[lparen_idx+1:rparen_idx])

