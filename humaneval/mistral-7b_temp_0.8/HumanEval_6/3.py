from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def is_open_paren(c: str) -> bool:
        return c == '('

    def is_close_paren(c: str) -> bool:
        return c == ')'

    def process_nested_parens(paren_string: str) -> List[int]:
        depth = 0
        results = []
        for char in paren_string:
            if is_open_paren(char):
                depth += 1
            elif is_close_paren(char):
                depth -= 1
            elif depth > 0:
                results.append(depth)
        return results

    return process_nested_parens(paren_string)

