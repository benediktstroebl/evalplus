from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result: List[int] = []
    for paren_string in paren_string.split(" "):
        stack = [paren_string]
        for paren in paren_string:
            if paren == "(":
                stack.append(paren)
            else:
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(paren)
        result.append(len(stack))
    return
