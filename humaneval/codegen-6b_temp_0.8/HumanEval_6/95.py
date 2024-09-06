from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    parens = {'(': 1, ')': -1}
    nest_level = 0
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            nest_level += 1
        if paren_string[i] == ')':
            nest_level -= 1

        if nest_level == 0 and i != len(paren_string)-1 and paren_string[i+1] not in parens:
            return 0
        elif nest_level > 0:
            stack.append(nest_level)
        elif nest_level < 0:
            level = stack.pop()
            if level > nest_level:
                return max(stack)
            elif level < nest_level:
                return max(stack) - 1

    return max(stack)

