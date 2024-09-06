from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result = []

    def traverse_nested_parens(
            left: int = 0, right: int = 0, level: int = 0, result: List[int] = result
    ) -> None:
        if left == right:
            result.append(level)
            return

        if left < right:
            traverse_nested_parens(left + 1, right, level + 1, result)
        else:
            traverse_nested_parens(left, right - 1, level + 1, result)

    traverse_nested_parens()
    return result

