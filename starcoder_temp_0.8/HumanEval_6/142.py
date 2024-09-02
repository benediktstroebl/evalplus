from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def calculate_depth(string: str) -> int:
        if not string:
            return 0
        if string.count("(") == 0 and string.count(")") == 0:
            return 0
        if string.count("(") == 0 and string.count(")") > 0:
            raise ValueError("Unbalanced string.")
        if string.count("(") > string.count(")"):
            return calculate_depth(string[string.find("(") + 1:]) + 1
        return calculate_depth(string[string.find(")") + 1:])
    return [calculate_depth(string) for string in paren_string.split(" ")]

