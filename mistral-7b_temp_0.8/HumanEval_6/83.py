from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_level = []

    def parse_paren_str(str_chunk: str, cur_level: int) -> int:
        """ Parses a string into its level of nesting.
        If str_chunk is empty string, return the level of nesting it is at.
        Otherwise, traverse the str_chunk recursively, and accumulate the
        maximum level of nesting encountered so far.
        """
        if str_chunk == '':
            return cur_level

        if str_chunk[0] == '(':
            cur_level += 1
            return parse_paren_str(str_chunk[1:], cur_level)
        else:
            cur_level -= 1
            return max(parse_paren_str(str_chunk[1:], cur_level), cur_level)

    for i in range(0, len(paren_string), 4):
        max_level.append(parse_paren_str(paren_string[i:i+4], 0))

    return max_level

