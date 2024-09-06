from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def dfs(curr_level: int, curr_paren_count: int, max_level: int, curr_depth: int) -> int:
        if curr_level >= max_level:
            return max(curr_depth, curr_paren_count)
        return max(dfs(curr_level + 1, curr_paren_count, max_level, curr_depth + 1), dfs(curr_level, curr_paren_count + 1, max_level, curr_depth))

    return [dfs(0, 0, len(paren_string), 0
