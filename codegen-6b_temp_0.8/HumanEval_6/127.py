from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result = []

    # Visit each character of the input string
    for c in paren_string:
        # If we encounter a open parenthesis, add 1 to result
        if c == '(':
            result.append(1)
        # If we encounter a closed parenthesis, lookup the index of the last element in result,
        # and add result[index-1] to result.
        elif c == ')':
            index = len(result) - 1
            result.append(result[index] + (result[index - 1] if index > 0 else 0))
            result.pop()

    return result

