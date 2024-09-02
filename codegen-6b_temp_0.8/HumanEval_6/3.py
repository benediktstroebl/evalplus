from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    start = 0
    level = 0
    result = []
    for i in range(len(paren_string)):
        if paren_string[i] == "(":
            stack.append(level)
            level += 1
            start = i + 1
        elif paren_string[i] == ")":
            if len(stack) == 0:
                result.append(level)
                break
            result.append(level)
            level -= 1
            stack.pop()

    for i in range(len(stack)):
        result.append(stack[-1 - i])

    return result

