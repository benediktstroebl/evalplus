from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # 1. Your code goes here.
    #
    # 2. For test purposes, this code may be useful
    #  print(
    #      "Expected result: [2, 3, 1, 3]\n"
    #      + "Your result is:   ",
    #      parse_nested_parens('(()()) ((())) () ((())()())')
    #  )

