from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    max_depth = 0
    for index, item in enumerate(paren_string):
        if item == '(':
            stack.append(index)
        if item == ')':
            if len(stack) > 0:
                # pop the stack until the last poped item is the index of the parenthesis
                while len(stack) > 0 and stack.pop() != index:
                    pass
                depth = len(stack)
                if depth > max_depth:
                    max_depth = depth
    return [max_depth] * len(paren_string)

