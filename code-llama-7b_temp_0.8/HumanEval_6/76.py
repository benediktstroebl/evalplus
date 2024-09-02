from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # The key here is to first split the whole string by spaces
    # So the result will be a list of strings, each of them is one "group" of nested parentheses.
    # Then iterate through the list and use a stack to keep track of the number of parentheses
    # whenever you encounter a left paren, push an item on the stack.
    # whenever you encounter a right paren, pop the stack.
    # At the end of each group, the length of the stack represents the level of nesting.
    # And since we start at level 1, we need to subtract 1 from the result.
    # At the end, flatten the list and return the result.
    result = []

    for group in paren_string.split():
        stack = []
        for paren in group:
            if paren == "(":
                stack.append(1)
            elif paren == ")":
                stack.pop()
        result.append(len(stack))

    return list(map(lambda x: x - 1, result))

