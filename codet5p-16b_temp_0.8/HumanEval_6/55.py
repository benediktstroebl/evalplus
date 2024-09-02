from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_string = paren_string.replace("(", " ").replace(")", " ").split()
    max_level = 0
    ans = []
    for s in paren_string:
        level = 0
        for char in s:
            if char == '(':
                level += 1
            elif char == ')':
                level -= 1
            else:
                raise ValueError("Unexpected character in string")
            if level < 0:
                raise ValueError("Unexpected nesting level")
            if max_level < level:
                max_level = level
                ans.append(max_level)

    return ans
