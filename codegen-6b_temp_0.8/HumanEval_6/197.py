from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    balance = 0
    stack = []
    current_max = 0
    for s in paren_string:
        if s == '(':
            stack.append(s)
            balance += 1
            if balance > current_max:
                current_max = balance
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
                balance -= 1
            else:
                return [0]
    if balance == 0:
        return [current_max]
    else:
        return [0]

