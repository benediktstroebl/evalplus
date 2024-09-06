from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def recursive_count(paren_string: str) -> int:
        count = 0
        for opening, closing in zip(paren_string.split(re.escape('(')), paren_string.split(re.escape(')'))):
            if opening == '(':
                count += 1
            if closing == ')':
                count -= 1
        return count

    def depth_first(paren_string: str) -> List[int]:
        if not paren_string:
            return []
        left, right = paren_string.split(' ')
        if left == '(':
            return [0]
        if right == ')':
            return [1]
        if len(left) == 1 and left.isdigit():
            return [int(left)]
        if len(right) == 1 and right.isdigit():
            return [int(right)]
        if left == '[' or right == ']':
            return [depth_first(left) + [depth_first(right)]]
        return [int(left), int(right)]

    return depth_first(paren_string)