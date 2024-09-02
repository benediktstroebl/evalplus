from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # # Version 1
    # lvl_list = []
    # for paren_group in paren_string.split():
    #     lvl = 0
    #     for paren in paren_group:
    #         if paren == '(':
    #             lvl += 1
    #         elif paren == ')':
    #             lvl -= 1
    #         else:
    #             raise ValueError(f"Unidentified character {paren}")
    #     lvl_list.append(lvl)
    # return lvl_list
    # # Version 2
    # return [max(0, level) for level in (
    #     sum(1 for c in paren_group if c == '(') - sum(1 for c in paren_group if c == ')')
    #     for paren_group in paren_string.split()
    # )]
    # Version 3
    return [
        max(0, sum(1 for c in paren_group if c == '(') - sum(1 for c in paren_group if c == ')'))
        for paren_group in paren_string.split()
    ]

