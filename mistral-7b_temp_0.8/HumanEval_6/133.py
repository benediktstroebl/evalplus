from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Recursive solution
    def inner(string: str) -> int:
        if string == "":
            return 0
        if len(string) == 1:
            if string == "(":
                return 1
            elif string == ")":
                return -1

        left, right = string[:1], string[1:]
        if left == "(" and right == ")":
            return inner(right) + 1
        elif left == ")" and right == "(":
            return inner(left) - 1
        elif left == "(" or right == ")":
            return max(0, inner(left) + 1, inner(right) + 1)
        elif left == ")" or right == "(":
            return max(0, inner(left) - 1, inner(right) - 1)

    return [inner(paren_string_part) for paren_string_part in paren_string.split(" ")]
