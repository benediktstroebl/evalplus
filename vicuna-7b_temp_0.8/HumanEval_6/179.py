from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    count = [0] * 5  # Initialize a list to keep count of nesting in each group
    stack = []  # Initialize a stack to keep track of nesting in nested parentheses
    for char in paren_string:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if stack[-1] == 1:
                count[stack.pop()] -= 1
            else:
                count[stack.pop()] += 1
                if count[stack.pop()] == 0:
                    stack.pop()  # Remove the last ( in the group
        else:
            if stack == []:
                count[0] += 1  # If there are no nested parentheses, increment the count of the first (
    return count