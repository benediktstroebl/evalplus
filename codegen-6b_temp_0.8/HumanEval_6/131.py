from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    if(len(paren_string) == 0):
        return []

    level = count_start_non_nested_paren_brackets(paren_string)
    bracket_closer_indices = find_matching_bracket_idxes(paren_string, 0)

    return [count_nested_parens(paren_string, bracket_closer_indices, level)]

