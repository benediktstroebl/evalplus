from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_string = paren_string.strip()
    stack = []
    paren_count = 0
    max_nested = []
    for i, c in enumerate(paren_string):
        if c == '(':
            if paren_count == 0:
                stack.append(i)
            paren_count += 1
        elif c == ')':
            paren_count -= 1
            if paren_count == 0:
                max_nested.append(len(stack))
                stack.pop()
        elif c =='':
            if paren_count == 0:
                max_nested.append(0)
    return max_nested

