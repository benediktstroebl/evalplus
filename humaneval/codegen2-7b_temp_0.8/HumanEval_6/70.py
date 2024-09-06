from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def helper(string):
        if string == "":
            return 0

        max_level = 0
        for c in string:
            if c == "(":
                max_level = max(max_level, helper(string[1:])) + 1
            elif c == ")":
                max_level -= 1
                if max_level == 0:
                    return 0

        return max_level

    return [helper(paren_string)] if paren_string!= "" else []
