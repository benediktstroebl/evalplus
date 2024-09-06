from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # TODO: Write your solution here
    stack = []
    depth = 0
    result = []
    for i in range(len(paren_string)+1):
        if paren_string[i] == '(':
            stack.append(depth)
            depth += 1
        if paren_string[i] == ')':
            if len(stack) == 0:
                print "depth = 0"
                return 0
            depth -= 1
            stack.pop()
    if depth == 0:
        print "depth = 0"
        return 0
    return result

