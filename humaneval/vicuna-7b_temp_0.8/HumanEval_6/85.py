from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def count_nesting(paren_string: str) -> int:
        nesting_count = 0
        last_paren = paren_string[-1]
        for open_paren in paren_string[:-1]:
            if open_paren == last_paren:
                nesting_count -= 1
            else:
                nesting_count = max(nesting_count, count_nesting(paren_string[0:]) - 1)
            last_paren = open_paren
        return nesting_count

    return list(map(count_nesting, paren_string.split()))

