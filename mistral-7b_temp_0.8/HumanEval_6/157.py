from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # base case
    if paren_string == "":
        return []

    # if there is only one set of parenthesis, return the level of nesting
    if paren_string.count('(') == paren_string.count(')'):
        return [(paren_string.count('(') - 1) // 2]

    # otherwise, split the string into two substrings of nested parentheses and
    # recursively get the level of nesting for each of the substrings
    # then add the two levels of nesting together to get the total level of nesting
    left_paren = paren_string.index('(')
    right_paren = paren_string.index(')', left_paren)
    left_half = paren_string[:left_paren]
    right_half = paren_string[right_paren + 1:]

    left_result = parse_nested_parens(left_half)
    right_result = parse_nested_parens(right_half)

    return left_result + right_result + [left_half.
