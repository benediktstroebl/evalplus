from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # The logic here is:
    # If we find a starting bracket, we append the index to a stack.
    # If we find a closing bracket, we pop off the index.
    # If we find an index with nothing on the stack, we know it is an invalid string.
    # If we find an index that is the same as the stack top, we know that it is the deepest level of nesting.
    # At the end of the function, the last index on the stack is the deepest level of nesting for the whole string.

    stack = []
    result = []

    for index, char in enumerate(paren_string):
        if char == '(':
            stack.append(index)
        elif char == ')':
            try:
                deepest_level = stack.pop()
                if index == deepest_level:
                    result.append(index)
            except IndexError:
                return []

    return result

