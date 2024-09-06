from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Brute force implementation
    # result = []
    # for paren_group in paren_string.split():
    #     count = 0
    #     for ch in paren_group:
    #         if ch == '(':
    #             count += 1
    #         elif ch == ')':
    #             count -= 1
    #     result.append(count)
    # return result

    # More pythonic implementation
    return [max([0] + [i for i, ch in enumerate(paren_group) if ch == '('])
            - max([0] + [i for i, ch in enumerate(paren_group) if ch == ')'])
            for paren_group in paren_string.split()]

