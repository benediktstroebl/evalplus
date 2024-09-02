from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    count = 0  # keep track of number of open parentheses
    stack = []  # keep track of nesting level
    max_level = 0  # keep track of maximum level of nesting

    for i in range(len(paren_string)):

        if paren_string[i] == '(':
            stack.append(count)
            count += 1
        elif paren_string[i] == ')':
            count -= 1
            if count == 0:
                stack.append(i)
                max_level = max(max_level, i - stack[-1])

    return list(reversed(stack))[1:len(stack) - 1]

