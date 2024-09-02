from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    count = 0
    for opening, closing in (((1, '(', ')'), (1, '[', ']'), (1, '{', '}')) if PY3 else (((2, '(', ')'), (2, '[', ']'), (2, '{' , '}'))):
        stack = []
        for char in paren_string:
            if char == opening:
                stack.append(1)
            elif char == closing:
                stack.append(0)
            elif char == '(':
                if len(stack) < 1:
                    count += 1
                stack.append(count)
            elif char == ')':
                if len(stack) < 0:
                    count -= 1
                stack.append(count)
        count = 0
    return count
